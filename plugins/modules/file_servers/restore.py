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

DOCUMENTATION = '''
---
module: commvault.ansible.file_servers.restore
short_description: To perform restore of a file server subclient.
description:
    - commvault.ansible.file_servers.restore can be used to perform a file server restore operation.
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
  - The name of the subclient.
  default: subclient named 'default'.
  type: str
  required: false
 content:
  description:
  - The path of the content that needs to be restored.
  type: str
  required: true
 in_place:
  description:
  - Whether the content needs to be restored in place i.e. restored back to the source location.
  choices: ['true','false']
  default: true
  type: bool
  required: false
 destination_path:
  description:
  - Destination path in case the content needs to be restored to another location.
  type: str
  required: false
 unconditional_overwrite:
  description:
  - Specifies whether data needs to be overwritten at the destination if the file already exists.
  choices: ['true','false']
  default: true
  type: bool
  required: false
author:
- Commvault Systems Inc 
'''

EXAMPLES = r'''
- name: Run a File System Restore for default subclient of default backupset, session file will be used.
  commvault.ansible.file_servers.restore:
    client: "client_name"
    content: "C:\path\of\content"

- name: Run a File System Restore for subclient 'user_subclient' of backupset 'user_backupset', session file will be used.
  commvault.ansible.file_servers.restore:
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    content: "C:\path\of\content"
    
- name: Run an In-Place File System Restore for subclient 'user_subclient' of backupset 'user_backupset'.
  commvault.ansible.file_servers.restore:
    webserver_hostname: "web_server_hostname"
    commcell_username: "user"
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    content: "C:\path\of\content"
    in_place: "yes"

- name: Run an In-Place File System Restore for subclient 'user_subclient' of backupset 'user_backupset' with agent_type of 'Linux File System'.
  commvault.ansible.file_servers.restore:
    webserver_hostname: "web_server_hostname"
    commcell_username: "user"
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    agent_type: "Linux File System"
    content: "C:\path\of\content"
    in_place: "yes"

'''

RETURN = r'''
job_id:
    description: Restore job ID
    returned: On success
    type: str
    sample: '2017'
'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():
    """Main method for this module."""

    module_args = dict(client=dict(type=str, required=True),
                       backupset=dict(type=str, required=False),
                       subclient=dict(type=str, required=False),
                       agent_type=dict(type=str, required=False),
                       content=dict(type=str, required=True),
                       in_place=dict(type=bool, required=False, default=True),
                       destination_path=dict(type=str, required=False),
                       unconditional_overwrite=dict(type=bool, required=False, default=True)
                       )

    module = CVAnsibleModule(argument_spec=module_args)
    module.result['changed'] = False

    try:
        client = module.commcell.clients.get(module.params.get('client'))
        agent_type = module.params.get('agent_type', 'File System')
        agent = client.agents.get(agent_type)
        backupset = agent.backupsets.get(agent.backupsets.default_backup_set if not module.params.get('backupset') else module.params.get('backupset'))
        subclient = backupset.subclients.get(backupset.subclients.default_subclient if not module.params.get('subclient') else module.params.get('subclient'))
        content = module.params.get('content')
        destination_path = module.params.get('destination_path')
        unconditional_overwrite = module.params.get('unconditional_overwrite')
        in_place = module.params.get('in_place')

        if destination_path is not None:
            in_place = False

        if in_place:
            restore = subclient.restore_in_place(
                paths=[content],
                overwrite=unconditional_overwrite
            )

        else:
            restore = subclient.restore_out_of_place(
                client=client,
                destination_path=destination_path,
                paths=[content],
                overwrite=unconditional_overwrite
            )

        module.result['job_id'] = str(restore.job_id)
        module.result['changed'] = True

        module.exit_json(**module.result)

    except Exception as e:
        module.result['msg'] = str(e)
        module.fail_json(**module.result)


if __name__ == "__main__":
    main()
