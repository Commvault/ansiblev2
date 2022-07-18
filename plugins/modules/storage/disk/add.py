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
module: commvault.ansible.storage.disk.add
short_description: Creates a disk storage
description: 
 - This module creates a disk storage in the CommCell
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
      - The name of the disk storage pool.
    type: str
    required: true
  media_agent:
    description:
      - The name of the media agent to create the disk storage for.
    type: str
    required: true
  mount_path:
    description:
      - The path of the disk storage.
    type: str
    required: true
  deduplication_db_path:
    description:
      - The path of the deduplication DB storage
    type: str
    required: true
author:
  - Commvault Systems Inc
'''

EXAMPLES = '''
- name: Creating disk storage
  commvault.ansible.storage.disk.add:
    name: "storage2"
    media_agent: "cv_mediaagent_1"
    mount_path: "D:\storage2"
    deduplication_db_path: "D:\ddb_path2"

- name: Creating disk storage
  commvault.ansible.storage.disk.add:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    name: "storage2"
    media_agent: "cv_mediaagent_1"
    mount_path: "D:\storage2"
    deduplication_db_path: "D:\ddb_path2"
'''

RETURN = r'''
name:
    description: The name of the disk storage created
    returned: Success
    type: str
    sample: 'storage2'
id:
    description: The ID of the disk storage created
    returned: Success
    type: str
    sample: '12'
'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():
    """Main method for this module."""

    module_args = dict(
        name=dict(type=str, required=True),
        media_agent=dict(type=str, required=True),
        mount_path=dict(type=str, required=True),
        deduplication_db_path=dict(type=str, required=True),
    )

    module = CVAnsibleModule(argument_spec=module_args)

    result = dict(
        changed=False,
        failed=False
    )

    param_name = module.params['name']
    param_media_agent = module.params['media_agent']
    param_mount_path = module.params['mount_path']
    param_ddb_path = module.params['deduplication_db_path']

    try:

        all_storage_pools = module.commcell.storage_pools
        all_media_agents = module.commcell.media_agents

        if all_storage_pools.has_storage_pool(param_name):
            module.exit_json(msg=f'Storage [{param_name}] already exists', **result)

        if not all_media_agents.has_media_agent(param_media_agent):
            module.fail_json(msg=f'Media agent [{param_media_agent}] does not exist')

        if module.check_mode:
            module.exit_json(**result)

        media_agent = all_media_agents.get(param_media_agent)

        new_storage_pool = all_storage_pools.add(
            storage_pool_name=param_name,
            mountpath=param_mount_path,
            media_agent=media_agent,
            ddb_ma=media_agent,
            dedup_path=param_ddb_path
        )

        result['changed'] = True
        result['name'] = new_storage_pool.storage_pool_name
        result['id'] = new_storage_pool.storage_pool_id

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=str(e), changed=False)

if __name__ == "__main__":
    main()
