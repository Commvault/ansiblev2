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
module: commvault.ansible.logout
short_description: Logs out of the Commcell.
description:
    - commvault.ansible.logout can be used to logout of the Commcell stored in the session file.
options:
author: 
- Commvault Systems Inc     
'''

EXAMPLES = r'''
- name: Log out of the Commcell
  commvault.ansible.logout:
'''

RETURN = r'''#'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule
from ansible_collections.commvault.ansible.plugins.module_utils.login.pre_login import PreLogin

def main():
    """Main method for this module."""

    module = CVAnsibleModule(argument_spec=dict())
    module.result['changed'] = False

    try:
        module.commcell.logout()

        # Reusing the clean_up() method for pre login to delete session file.
        pre_login = PreLogin()
        pre_login.clean_up()

        module.result['changed'] = True

        module.exit_json(**module.result)

    except Exception as e:
        module.result['msg'] = str(e)
        module.fail_json(**module.result)


if __name__ == "__main__":
    main()
