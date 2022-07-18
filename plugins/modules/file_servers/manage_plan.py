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
module: commvault.ansible.file_servers.manage_plan
short_description: To change the plan associated to the client, backupset or subclient.
description:
    - commvault.ansible.file_servers.manage_plan can be used to change the server plan associated at the client, backupset or subclient level.
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
 client:
  description:
  - The name of the client.
  type: str
  required: true 
 plan:
  description:
  - The name of the server plan which needs to be associated to the entity.
  type: str
  required: true 
 backupset:
  description:
  - The name of the backupset.  
  type: str
  required: false     
 subclient:
  description:
  - The name of the subclient.  
  type: str
  required: false 
'''

EXAMPLES = r'''
- name: Associate a client to plan 'server plan', session file will be used.
  commvault.ansible.file_servers.manage_plan:
    client: "client_name"
    plan: "server plan"

- name: Associate a user created subclient to plan 'server plan'.
  commvault.ansible.file_servers.manage_plan:
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    plan: "server plan"
    
- name: Associate a user created subclient to plan 'server plan'.
  commvault.ansible.file_servers.manage_plan:
    webserver_hostname: "web_server_hostname"
    commcell_username: "user"
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    plan: "server plan"
author:
- Commvault Systems Inc 
'''

RETURN = r'''#'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():
    """Main method for this module."""

    module_args = dict(
        client=dict(type=str, required=True),
        plan=dict(type=str, required=True),
        backupset=dict(type=str, required=False),
        subclient=dict(type=str, required=False)
    )

    module = CVAnsibleModule(argument_spec=module_args, required_by={'subclient': 'backupset'})
    module.result['changed'] = False

    try:
        plan = module.commcell.plans.get(module.params.get('plan'))
        client = module.commcell.clients.get(module.params.get('client'))
        agent = client.agents.get('File System')
        backupset = agent.backupsets.get(agent.backupsets.default_backup_set if not module.params.get('backupset') else module.params.get('backupset'))
        if module.params.get('subclient'):
            subclient = backupset.subclients.get(module.params.get('subclient'))
            subclient.plan = plan
        else:
            backupset.plan = plan
        module.result['changed'] = True

        module.exit_json(**module.result)

    except Exception as e:
        module.result['msg'] = str(e)
        module.fail_json(**module.result)


if __name__ == "__main__":
    main()
