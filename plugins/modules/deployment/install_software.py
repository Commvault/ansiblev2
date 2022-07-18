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
module: commvault.ansible.deployment.install_software
short_description: To perform Push Installation from the Commserve
description: 
    - This module performs a Fresh Push Installation to Client Machine from the CommCell
    - commvault.ansible.deployment.install_software module can be used in playbooks to perform Push Installs to Clients

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
    
    os_type:
        description:
            - Client machine operating system category 
        type: str
        required: true
        choices: ["windows", "unix"]

    client_computers:
        description:
            - List of Hostnames of the Client Computers to perform a Push installion 
            - Provide Windows Hostnames (or) Unix Hostnames but never both together
        type: list
        required: true
    
    windows_package:
        description:
            - list of windows features to be installed
        type: list (List of enum keys mentioned below)
        required: false
        default: None
        choices: ["ACTIVE_DIRECTORY", "CLOUD_APPS", "DOMINO_DATABASE", "EXCHANGE", "FILE_SYSTEM", "MEDIA_AGENT",
            "SHAREPOINT", "ORACLE", "POSTGRESQL", "SQLSERVER", "VIRTUAL_SERVER", "VSS_PROVIDER", "WEB_CONSOLE", "TEST_AUTOMATION",
            "PYTHON_SDK", "COMMSERVE_LITE", "CONTENT_ANALYZER"]
    
    unix_packages:
        description:
            - list of unix features to be installed
        type: list (List of enum keys mentioned below)
        required: false
        default: None
        choices: ["CASSANDRA", "CLOUD_APPS", "DOMINO_DATABASE", "FILE_SYSTEM", "FILE_SYSTEM_FOR_IBMI", 
            "FILE_SYSTEM_FOR_OPEN_VMS", "MEDIA_AGENT", "ORACLE", "POSTGRESQL", "SAPHANA", "SQLSERVER", "VIRTUAL_SERVER",
            "TEST_AUTOMATION", "PYTHON_SDK", "CONTENT_ANALYZER"]

    username:
        description:
            - username of the machine to install features on
        type: str
        required: false
        default: None
    
    password:
        description:
            - Password of the machine to install features on
        type: str
        required: false
        default: None

    install_path:
        description:
            - Install to a specified path on the client
        type: str
        required: false
        default: None

    client_group_name:
        description:
            - List of the client groups for the client
        type: list
        required: false
        default: None

    storage_policy_name:
        description:
            - Storage policy for the default subclient
        type: str
        required: false
        default: None
    
    sw_cache_client:
        description:
            - Remote Cache Client Name/ Over-riding Software Cache
        type: str
        required: false
        default: None

    ma_index_cache_loaction:
        description:
            - Index Cache location of the Media Agent package
        type: str
        required: false
        default: None

    wait_for_job_completion:
        description:
            - Will wait for Download Job to Complete
        type: bool
        required: false
        default: True

notes:
    - windows_package option required only for Windows Client Installations & None for Unix Client Installations
    - unix_packages option required only for Unix Client Installations & None for Windows Client Installations
    
'''

EXAMPLES = '''
# Run a Push Installation to the client from Commserver.

- name: "INSTALL_SOFTWARE/PUSH_INSTALL"
  commvault.ansible.deployment.install_software:
    os_type: "windows"
    client_computers:
      - hostname1.example.com
      - x.x.x.x
    windows_packages:
      - FILE_SYSTEM
      - PYTHON_SDK
    username: "domain\\username"
    password: "password"
    client_group_name:
      - random_group1
      - random_group2
      - random_group3
    install_path: "D:\\Random"
    sw_cache_client: "RemoteCacheClient1"
    wait_for_job_completion: False

- name: "INSTALL_SOFTWARE/PUSH_INSTALL_WINDOWS"
  commvault.ansible.deployment.install_software:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    os_type: "unix"
    client_computers:
      - hostname1.example.com
      - x.x.x.x
    windows_packages:
      - FILE_SYSTEM
      - PYTHON_SDK
    username: "domain\\username"
    password: "password"
    client_group_name:
      - random_group1
      - random_group2
      - random_group3
    install_path: "D:\\Random"
    sw_cache_client: "RemoteCacheClient1"
    wait_for_job_completion: True

- name: "INSTALL_SOFTWARE/PUSH_INSTALL_UNIX"
  commvault.ansible.deployment.install_software:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    os_type: "unix"
    client_computers:
      - hostname1.example.com
      - x.x.x.x
    unix_packages:
      - MEDIA_AGENT
      - FILE_SYSTEM
    username: "root"
    password: "password"
    client_group_name:
      - random_group1
      - random_group2
      - random_group3
    install_path: "/opt/commvault/ansibledeployment"
    ma_index_cache_location: "/opt/commvault/ma_index_cache"
    sw_cache_client: "RemoteCacheClient1"

notes: 
    Either Windows Packages can be provided or Unix Packages but never both together; 
    Cross platform(Windows & Unix) Push Installation not Supported

'''

RETURN = r'''
job_id:
    description: Push Software Job ID
    returned: success
    type: str
    sample: '2016'

'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule
try:
    from base64 import b64encode
    from cvpysdk.deployment.deploymentconstants import UnixDownloadFeatures, WindowsDownloadFeatures
except ModuleNotFoundError:
    pass


def main():
    try:
        windows_options = [e.name for e in WindowsDownloadFeatures]
        unix_options = [e.name for e in UnixDownloadFeatures]
        operating_system_types = ["windows", "unix"]

        module_args = dict(
            os_type=dict(type=str, choices=operating_system_types, required=True),
            client_computers=dict(type=list, required=True),
            windows_packages=dict(type=list, required=False, choices=windows_options, default=None),
            unix_packages=dict(type=list, required=False, choices=unix_options, default=None),
            username=dict(type=str, required=False, default=None),
            password=dict(type=str, required=False, default=None),
            install_path=dict(type=str, required=False, default=None),
            client_group_name=dict(type=list, required=False, default=None),
            storage_policy_name=dict(type=str, required=False, default=None),
            sw_cache_client=dict(type=str, required=False, default=None),
            wait_for_job_completion=dict(type=bool, required=False, default=True),
            ma_index_cache_location=dict(type=str, required=False, default=None),
        )
                        
        module = CVAnsibleModule(argument_spec=module_args)
        encoded_password=final_download_decision=os_to_download=None

        os_type=module.params['os_type']
        client_computers=module.params['client_computers']
        windows_packages=module.params['windows_packages']
        unix_packages=module.params['unix_packages']
        username=module.params['username']
        plain_password=module.params['password']
        install_path=module.params['install_path']
        client_group_name=module.params['client_group_name']
        storage_policy_name=module.params['storage_policy_name']
        sw_cache_client=module.params['sw_cache_client']
        wait_for_job_completion = module.params['wait_for_job_completion']
        ma_index_cache_location = module.params['ma_index_cache_location']

        windows_features=unix_features=None

        if not client_computers:
            raise Exception("Please provide Hostnames of either Windows or Unix Computers to install the packages")
        
        if not os_type:
            raise Exception("Please specify the Operating System Category on which you want to Push the packages to")

        if "windows" in os_type.lower():
            windows_features=[]
            for package in windows_packages:
                try:
                    windows_features.append(WindowsDownloadFeatures[package].value)
                
                except KeyError:
                    raise Exception("Please provide Correct/Appropriate value for the Windows Package: " + str(package))

        elif "unix" in os_type.lower():
            unix_features=[]
            for package in unix_packages:
                try:
                    unix_features.append(UnixDownloadFeatures[package].value)
                
                except KeyError:
                    raise Exception("Please provide Correct/Appropriate value for the Unix Package: " + str(package))
        
        else:
            raise Exception("Please provide the appropriate os type: windows or Unix")

        if plain_password:
            encoded_password=b64encode(plain_password.encode()).decode()

        install_job = module.commcell.install_software(
                        client_computers=client_computers,
                        windows_features=windows_features,
                        unix_features=unix_features,
                        username=username,
                        password= encoded_password,
                        install_path=install_path,
                        client_group_name=client_group_name,
                        storage_policy_name=storage_policy_name,
                        sw_cache_client=sw_cache_client,
                        index_cache_location=ma_index_cache_location)
        
        job_id = install_job.job_id
        module.result['job_id'] = str(job_id)

        if wait_for_job_completion:
            if not install_job.wait_for_completion():
                module.result['failed'] = True
                job_status = install_job.delay_reason
                raise Exception(str(job_status))
        
        module.result['failed'] = False
        module.result['changed'] = False
        module.exit_json(**module.result)
    
    except Exception as exp:
        module.result['failed'] = True
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()