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
module: commvault.ansible.storage.disk.detail
short_description: Gets details of a disk storage
description: 
 - This module gets details of a given disk storage
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
author:
  - Commvault Systems Inc
'''

EXAMPLES = '''
- name: "Getting details of disk storage"
  commvault.ansible.storage.disk.detail:
    name: "storage2"

- name: "Getting details of disk storage"
  commvault.ansible.storage.disk.detail:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    name: "storage2"
'''

RETURN = r'''
detail:
    description: Details of the disk storage
    returned: Success
    type: dict
'''

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

        all_storage_pools = module.commcell.storage_pools

        if not all_storage_pools.has_storage_pool(param_name):
            module.exit_json(msg=f'Storage pool [{param_name}] does not exist', **result)

        if module.check_mode:
            module.exit_json(**result)

        storage_pool_detail = all_storage_pools.get(param_name).storage_pool_properties

        result['detail'] = storage_pool_detail

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=str(e), changed=False)

if __name__ == "__main__":
    main()
