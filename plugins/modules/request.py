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
module: commvault.ansible.request
short_description: Makes a HTTP request on the Commserver API
description: 
    - This module makes HTTP requests to the Commserver API

options:
    webserver_hostname:
        description:
            - Hostname of the Web Server. 
        type: str
        required: false

    commcell_username:
        description:
            - Username 
        type: str
        required: false    

    commcell_password:
        description:
            - Password 
        type: str
        required: false

    method:
        description:
            - Web method to use to make the request
        type: str
        required: true
        choices: ["GET", "POST", "PUT", "DELETE"]

    url:
        description:
            - The web URL or service to run the HTTP request on. Use "{0}" to autopopulate webconsole URL
        type: str
        required: true

    payload:
        description:
            - Dictionary consisting of JSON payload to pass to the HTTP Request
        type: dict
        required: False
        default: None
    
'''

EXAMPLES = '''
- name: "REQUEST"
  commvault.ansible.request:
    method: 'GET'
    url: '{0}/cvdrbackup/info'
  register: response

- name: "REQUEST_RESTART_SERVICES"
    commvault.ansible.request:
    method: 'POST'
    url: '{0}/services/action/restart'
    payload:
      "action": 2
      "client": 
        "clientName": "client"
      "services":
        "allServices": true

- name: "REQUEST"
  commvault.ansible.request:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    method: 'GET'
    url: '{0}/cvdrbackup/info'
  register: response

'''

RETURN = r'''
response:
    description: Response of the HTTP request
    returned: success
    type: dict 
    sample:
      errorCode: 0
      errorMessage: ""

'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():

    try:
        module_args =  dict(method=dict(type=str, required=True),
                            url=dict(type=str, required=True),
                            payload=dict(type=dict, required=False, default=None),
                            )

        module = CVAnsibleModule(argument_spec=module_args)

        method = module.params['method']
        url = module.params['url']
        payload =  module.params['payload']

        WEB_METHODS = ["GET", "POST", "PUT", "DELETE"]

        if method is None or method not in WEB_METHODS:
            raise Exception("Please provide an appropriate Web Method")

        if url is None:
            raise Exception("Please provide an appropriate Web URL")

        url = url.format(module.commcell._web_service)
        cvpysdk_object = module.commcell._cvpysdk_object

        flag, response = cvpysdk_object.make_request(method=method,
                                                     url=url,
                                                     payload=payload)

        if not flag:
            raise Exception("Response was not success")

        module.result['response'] = response.json()
        module.result['failed'] = False
        module.result['changed'] = False
        module.exit_json(**module.result)

    except Exception as exp:
        module.result['failed'] = True
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()