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
module: commvault.ansible.plans.delete
short_description: Deletes a plan
description: 
 - This module deletes a Plan in the CommCell
options:
  webserver_hostname:
    description:
      - Hostname of the Web Server. 
    type: str
    required: false
  webserver_username:
    description:
      - Webserver username 
    type: str
    required: false
  webserver_password:
    description:
      - Webserver password 
    type: str
    required: false
  name:
    description:
      - The name of the plan to delete.
    type: str
    required: true
author:
  - Commvault Systems Inc
'''

EXAMPLES = '''
- name: Deleting plan
  commvault.ansible.plans.delete:
    name: "Plan 1"

- name: Deleting plan
  commvault.ansible.plans.delete:
    webserver_hostname: "web_server_hostname" 
    webserver_username: "user"  
    webserver_password: "password"
    name: "Plan 1"
'''

RETURN = r''' # '''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():
    """Main method for this module."""

    module_args = dict(
        name=dict(type=str, required=True)
    )

    module = CVAnsibleModule(argument_spec=module_args)

    result = dict(
        changed=False,
        failed=False
    )

    param_name = module.params['name']

    try:

        all_plans = module.commcell.plans

        if not all_plans.has_plan(param_name):
            module.exit_json(msg=f'Plan [{param_name}] does not exist', **result)

        if module.check_mode:
            module.exit_json(**result)

        all_plans.delete(
            plan_name=param_name
        )

        result['changed'] = True

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=str(e), changed=False)

if __name__ == "__main__":
    main()
