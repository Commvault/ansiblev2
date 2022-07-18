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

"""File for class CVAnsibleModule, class for all Commvault Ansible Modules.

CVAnsibleModule is the only class defined in this file.

CVAnsibleModule: Derived class from AnsibleModule Base class, representing a Commvault Ansible Module.

CVAnsibleModule:
    __init__()  --  Initializes a Commvault Ansible Module.
    __del__()   --  Called when the instance is about to be destroyed, saves the Commcell object to the session file.
    _login()    --  Logs in to Commcell.
    exit_json() --  Handles module exit.

"""

import pickle
import os
import stat

from .login.pre_login import (
    FILE_PATH,
    SESSION_ID
)
from ansible.module_utils.basic import AnsibleModule


class CVAnsibleModule(AnsibleModule):
    """Class representing a Commvault Ansible Module."""

    def __init__(self, argument_spec, override=False, **kwargs):
        """"Initializes a Commvault Ansible Module.

            Args:
                argument_spec   (dict)  --  Arguments that are specific to the module, keys is argument name,
                value is a dictionary of keys type and  required, value is built in type and bool respectively.

                override (bool)  --  Overrides the existing requirements for modules.
                    default :   False

        """

        self.argument_spec = argument_spec
        self.commcell = None
        self.session_file_path = None
        self.result = {}
        self.login_args = {
            'webserver_hostname': dict(type=str, required=False),
            'commcell_username': dict(type=str, required=False),
            'commcell_password': dict(type=str, required=False, no_log=True),
            'webserver_username': dict(type=str, required=False),
            'webserver_password': dict(type=str, required=False, no_log=True),
            'auth_token': dict(type=str, required=False),
            'session_id': dict(type=str, required=False)
        }

        # By default we will always try to create a Commcell object.
        if override:
            return super().__init__(argument_spec=self.argument_spec, supports_check_mode=True)

        try:
            for key, value in self.login_args.items():
                if key not in self.argument_spec:
                    self.argument_spec.update({key: value})

            super().__init__(argument_spec=self.argument_spec, supports_check_mode=True, **kwargs)

            # Verifying credentials & auth_token manually instead of built in mutually_exclusive, required_by etc.
            creds = all([self.params.get(key) for key in ['webserver_hostname', 'commcell_username', 'commcell_password']]) \
                        ^ all([self.params.get(key) for key in ['webserver_hostname', 'webserver_username', 'webserver_password']])
            auth_token = all([self.params[key] for key in ['webserver_hostname', 'auth_token']])

            # Figure out the session ID
            session_id = SESSION_ID if not self.params.get('session_id') else self.params.get('session_id')
            self.session_file_path = FILE_PATH.format(SESSION_ID=session_id)

            if creds and auth_token:
                result = {"msg": "Both auth_token & commcell_username\\commcell_password provided."}
                self.fail_json(**result)

            # 1st priority --> is for module level arguments
            if creds or auth_token:
                self.commcell = self._login(**self.params)

            # 2nd priority  --> is for session file.
            else:
                with open(self.session_file_path, "rb") as fh:
                    self.commcell = pickle.load(fh)

        except FileNotFoundError:
            result = {"msg": f"Failed to open session file {self.session_file_path}, it might not exist."}
            self.fail_json(**result)

    def __del__(self):
        """Called when the instance is about to be destroyed, saves the Commcell object to the session file."""

        # Avoiding exceptions in __del__ as they will be logged to stderr.
        if self.session_file_path:
            with open(self.session_file_path, 'wb') as fh:
                pickle.dump(self.commcell, fh)
        os.chmod(self.session_file_path, stat.S_IRWXU)  # SET READ, WRITE & EXECUTE PERMISSIONS FOR OWNER

    def _login(self, *args, **kwargs):
        """Login to Commcell and return object of Commcell.

            \*\*kwargs  (dict)  --  Optional arguments.

                Available kwargs Options:

                    webserver_hostname  (str)   --  Hostname of the Web Server.

                    commcell_username  (str)   --  Username for log in to the Commcell console.

                    commcell_password  (str)   --  Plain-text password for log in to the console.

                    authtoken           (str)   --  QSDK/SAML token for log in to the console.

        """
        try:
            from cvpysdk.commcell import Commcell, SDKException

            return Commcell(
                webconsole_hostname=kwargs['webserver_hostname'],
                commcell_username=kwargs.get('commcell_username') or kwargs.get('webserver_username'),
                commcell_password=kwargs.get('commcell_password') or kwargs.get('webserver_password'),
                authtoken=kwargs.get('auth_token')
            )

        except (ModuleNotFoundError, ImportError):
            result = {"changed": False, "msg": "Unable to import CVPySDK, please ensure it is installed on the node"}
            self.fail_json(**result)

        except SDKException as e:
            result = {"changed": False, "msg": str(e)}
            self.fail_json(**result)

    def exit_json(self, *args, **kwargs):
        """Ensures that return variables 'changed' and 'failed' have been set."""
        assert "changed" in kwargs, "Module developed is missing return variable(s)."
        super().exit_json(*args, **kwargs)
