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
module: commvault.ansible.file_servers.manage_content
short_description: To update the properties of a file server at subclient level.
description:
 - commvault.ansible.file_servers.manage_content can be used to update the content, filters and exceptions of a File System subclient. 
 - keys for 'update' are 'content', 'filter_content', 'exception_content' & will ALWAYS OVERWRITE existing values.
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
 update:
  description:
  - A dictionary of updates to make where update is a dictionary with key is property name & value is property value.
  - choices specifies the supported key values.
  choices: ['content', 'filter_content', 'exception_content']
  type: dict
  required: true 
author:
- Commvault Systems Inc        
'''

EXAMPLES = r'''
- name: Update a File System subclient's content and filter, session file would be used.
  commvault.ansible.file_servers.manage_content:
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    update:
        content:
            - C:\ANSIBLE_PATH1
            - C:\ANSIBLE_PATH2
        filter_content:
            - C:\ANSIBLE_PATH1\FILTER1
            - C:\ANSIBLE_PATH1\FILTER2      

- name: Update a File System subclient's content and filter.
  commvault.ansible.file_servers.manage_content:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    update:
        content:
            - C:\ANSIBLE_PATH1
            - C:\ANSIBLE_PATH2
        filter_content:
            - C:\ANSIBLE_PATH1\FILTER1
            - C:\ANSIBLE_PATH1\FILTER2                  
'''
RETURN = r'''#'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule

supported_properties = ['content', 'filter_content', 'exception_content']


def main():

    module_args = dict(
        client=dict(type=str, required=True),
        backupset=dict(type=str, required=False),
        subclient=dict(type=str, required=False),
        update=dict(type=dict, required=True)
    )

    module = CVAnsibleModule(argument_spec=module_args)
    module.result['changed'] = False

    try:
        client = module.commcell.clients.get(module.params.get('client'))
        agent = client.agents.get('File System')
        backupset = agent.backupsets.get(agent.backupsets.default_backup_set if not module.params.get('backupset') else module.params.get('backupset'))
        subclient = backupset.subclients.get(backupset.subclients.default_subclient if not module.params.get('subclient') else module.params.get('subclient'))
        update = module.params.get('update')

        if not all([property if property in supported_properties else False for property in update.keys()]):
            raise ValueError("Unsupported key supplied in 'update'")

        for property, new_property_value in update.items():
            if sorted(getattr(subclient, property)) != sorted(new_property_value):
                setattr(subclient, property.lower(), new_property_value)
                module.result['changed'] = True

        module.exit_json(**module.result)

    except Exception as e:
        module.result['msg'] = str(e)
        module.fail_json(**module.result)


if __name__ == "__main__":
    main()
