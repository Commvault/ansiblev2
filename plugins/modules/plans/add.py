# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------
# Copyright Commvault Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------


DOCUMENTATION = r'''
---
module: commvault.ansible.plans.add
short_description: Creates a plan
description: 
 - This module creates a Plan in the CommCell
options:
  webserver_hostname:
    description:
      - Hostname of the Web Server. 
    type: str
    required: false
  commcell_username:
    description:
      - Commcell username 
    type: str
    required: false 
  commcell_password:
    description:
      - Commcell password 
    type: str
    required: false
  name:
    description:
      - The name of the plan.
    type: str
    required: true
  storage_pool_name:
    description:
      - The name of the storage to use for the plan.
    type: str
    required: true
  type:
    description:
      - The type of plan to create.
    type: str
    default: Server
    required: false
    choices: ["Server", "Laptop", "ExchangeUser"]
  rpo_minutes:
    description:
      - The Recovery Point Objective time in minutes for the plan. Default is 1440 minutes (24 hours)
    type: int
    default: 1440
    required: false
author:
- Commvault Systems Inc
'''

EXAMPLES = '''
- name: Creating a plan
  commvault.ansible.plans.add:
    name: "Plan 1"
    storage_pool_name: "storage2"

- name: Creating a plan with 7 days RPO
  commvault.ansible.plans.add:
    name: "Plan 1"
    storage_pool_name: "storage2"
    rpo_minutes: 10080

- name: Creating a "Server" plan with 2 days RPO
  commvault.ansible.plans.add:
    name: "Plan 1"
    type: "Server"
    storage_pool_name: "storage2"
    type: "Server"
    rpo_minutes: 2880

- name: Creating a "Server" plan with 2 days RPO
  commvault.ansible.plans.add:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    name: "Plan 1"
    type: "Server"
    storage_pool_name: "storage2"
    rpo_minutes: 2880
'''

RETURN = r'''
name:
    description: The name of the plan created
    returned: Success
    type: str
    sample: 'Plan 1'
id:
    description: The ID of the plan created
    returned: Success
    type: str
    sample: '2'
'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():
    """Main method for this module."""

    module_args = dict(
        name=dict(type=str, required=True),
        storage_pool_name=dict(type=str, required=True),
        type=dict(type=str, required=False, choices=['Server', 'Laptop', 'ExchangeUser'], default='Server'),
        rpo_minutes=dict(type=int, required=False, default=1440),
    )

    module = CVAnsibleModule(argument_spec=module_args)

    result = dict(
        changed=False,
        failed=False
    )

    param_name = module.params['name']
    param_type = module.params['type']
    param_storage_pool_name = module.params['storage_pool_name']
    param_rpo_minutes = module.params['rpo_minutes']

    try:

        all_plans = module.commcell.plans
        all_storage_pools = module.commcell.storage_pools

        if all_plans.has_plan(param_name):
            module.exit_json(msg=f'Plan [{param_name}] already exists', **result)

        if not all_storage_pools.has_storage_pool(param_storage_pool_name):
            module.fail_json(msg=f'Storage pool [{param_storage_pool_name}] does not exist')

        if module.check_mode:
            module.exit_json(**result)

        new_plan = all_plans.add(
            plan_name=param_name,
            plan_sub_type=param_type,
            storage_pool_name=param_storage_pool_name
        )

        result['changed'] = True
        result['name'] = new_plan.plan_name
        result['id'] = new_plan.plan_id

        plan_schedule_policy = new_plan.schedule_policies['data']

        # Setting the RPO configuration for the plan schedule policy
        plan_schedule_policy.modify_schedule(
            {
                'pattern': {
                    'freq_type': 'After_job_completes',  # For minutes/hours frequency we set a schedule pattern of type "continuous"
                    'freq_interval': param_rpo_minutes,
                    'active_end_time': '23:59',
                    'freq_recurrence_factor': 1
                }
            },
            schedule_name='Incremental backup schedule'
        )

        # Adding all agents to the plan schedule policy
        plan_schedule_policy.update_app_groups(
            [
                {"appGroupId": 12}, {"appGroupId": 129}, {"appGroupId": 114},
                {"appGroupId": 6}, {"appGroupId": 2}, {"appGroupId": 13},
                {"appGroupId": 8}, {"appGroupId": 104}, {"appGroupId": 90},
                {"appGroupId": 7}, {"appGroupId": 128}, {"appGroupId": 68},
                {"appGroupId": 67}, {"appGroupId": 100}, {"appGroupId": 3},
                {"appGroupId": 101}, {"appGroupId": 135}, {"appGroupId": 1},
                {"appGroupId": 115}, {"appGroupId": 10}, {"appGroupId": 11},
                {"appGroupId": 83}, {"appGroupId": 111}, {"appGroupId": 14},
                {"appGroupId": 5}, {"appGroupId": 134}
            ],
            'include'
        )

        # By default both FULL and Synthetic FULL backup schedules are created always,
        # hence deleting the FULL backup schedule
        new_plan.disable_full_schedule()

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=str(e), changed=result['changed'])

if __name__ == "__main__":
    main()
