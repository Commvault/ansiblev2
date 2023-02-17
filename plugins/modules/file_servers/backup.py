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
module: commvault.ansible.file_servers.backup
short_description: To perform backup of a file server subclient.
description:
    - commvault.ansible.file_servers.backup can be used to perform file server backup operation.
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
  -  The name of the Client.
  type: str
  required: true
 agent_type:
  description:
  - The agent type
  type: str
  required: false
 backupset:
  description:
  - The name of the backupset.
  default: default backupset
  type: str
  required: false
 subclient:
  description:
  -  The name of the subclient.    
  default: subclient named default.
  type: str
  required: false
 backup_level:
  description:
  -  backup level    
  default: incremental
  type: str
  required: false
author:
- Commvault Systems Inc        
'''

EXAMPLES = '''
- name: Run a File System Backup for default subclient of default backupset, session file would be used.
  commvault.ansible.file_servers.backup:
    client: "client_name"

- name: Run a File System Backup for subclient 'user_subclient' of backupset 'user_backupset', session file would be used.
  commvault.ansible.file_servers.backup:
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
        
- name: Run a File System Backup for default subclient of default backupset.
  commvault.ansible.file_servers.backup:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    client: "client_name"

- name: Run a File System Backup for subclient 'user_subclient' of backupset 'user_backupset'.
  commvault.ansible.file_servers.backup:
    webserver_hostname: "web_server_hostname"
    commcell_username: "user"  
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"

- name: Run a File System Backup for subclient 'user_subclient' of backupset 'user_backupset' with agent_type of 'Linux File System'.
  commvault.ansible.file_servers.backup:
    webserver_hostname: "web_server_hostname"
    commcell_username: "user"
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    agent_type: "Linux File System"

'''

RETURN = r'''
job_id:
    description: Backup job ID
    returned: On success
    type: str
    sample: '2016'
'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():
    """Main method for this module."""

    module_args = dict(
        client=dict(type=str, required=True),
        backupset=dict(type=str, required=False),
        subclient=dict(type=str, required=False),
        backup_level=dict(type=str, required=False),
        agent_type=dict(type=str, required=False)
    )

    module = CVAnsibleModule(argument_spec=module_args)
    module.result['changed'] = False

    try:
        client = module.commcell.clients.get(module.params.get('client'))
        agent_type = module.params.get('agent_type', 'File System')
        agent = client.agents.get(agent_type)
        backupset = agent.backupsets.get(agent.backupsets.default_backup_set if not module.params.get('backupset') else module.params.get('backupset'))
        subclient = backupset.subclients.get(backupset.subclients.default_subclient if not module.params.get('subclient') else module.params.get('subclient'))
        backup_level = module.params.get('backup_level', 'incremental')
        backup = subclient.backup(backup_level=backup_level)
        module.result['job_id'] = str(backup.job_id)
        module.result['changed'] = True

        module.exit_json(**module.result)

    except Exception as e:
        module.result['msg'] = str(e)
        module.fail_json(**module.result)


if __name__ == "__main__":
    main()
