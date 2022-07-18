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
module: commvault.ansible.deployment.download_software
short_description: To perform Download Software on Commserve
description: 
    - This module Downloads Media/Latest Payload from the Internet
    - commvault.ansible.deployment.download_software module can be used in playbooks to perform Download Software on CS

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

    download_option:
        description:
            - Download option to download software
        type: str
        required: false
        choices: ["LATEST_SERVICEPACK", "LATEST_HOTFIXES", "SERVICEPACK_AND_HOTFIXES"]
        default: "LATEST_SERVICEPACK"

    os_list:
        description:
            - list of windows/unix packages to be downloaded
        type: list
        required: false
        choices: ["WINDOWS_32", "WINDOWS_64", "UNIX_AIX", "UNIX_AIX32", "UNIX_MAC", "UNIX_FREEBSD86", "UNIX_FREEBSD64",
            "UNIX_HP", "UNIX_LINUX86", "UNIX_LINUX64", "UNIX_S390", "UNIX_S390_31", "UNIX_PPC64", "UNIX_SOLARIS86", 
            "UNIX_SOLARIS64", "UNIX_SOLARIS_SPARC", "UNIX_SOLARIS_SPARC86", "UNIX_LINUX64LE"]
        default: None
    
    service_pack:
        description:
            - service pack to be downloaded
        type: int
        required: false
        default: None

    cu_number:
        description:
            - maintenance release number
        type: int
        required: false
        default: 0
    
    sync_cache:
        description:
            - Download/Sync the Remote Cache
        type: bool
        required: false
        default: True

    wait_for_job_completion:
        description:
            - Will wait for Download Job to Complete
        type: bool
        required: false
        default: True
        
notes:
    - Service_pack option required only with the Download Option : "SERVICEPACK_AND_HOTFIXES"

'''

EXAMPLES = '''
# Run a Download Job on the Commserver.

- name: "DOWNLOAD_SOFTWARE"
  commvault.ansible.deployment.download_software:
    download_option: "LATEST_SERVICEPACK"
    os_list:
      - WINDOWS_64
      - UNIX_LINUX64
    sync_cache: False
    wait_for_job_completion: False

- name: "DOWNLOAD_SOFTWARE"
  commvault.ansible.deployment.download_software:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    download_option: "LATEST_SERVICEPACK" (or)  "LATEST_HOTFIXES"
    os_list:
      - WINDOWS_64
      - UNIX_LINUX64
    sync_cache: False

- name: "DOWNLOAD_SOFTWARE"
  commvault.ansible.deployment.download_software:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    download_option: "SERVICEPACK_AND_HOTFIXES"
    os_list:
      - WINDOWS_64
      - UNIX_LINUX64
    service_pack: 23
    cu_number: 2
    sync_cache: False
    wait_for_job_completion: False
      
'''

RETURN = r'''
job_id:
    description: Download Software Job ID
    returned: success
    type: str 
    sample: '2016'

'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule
try:
    from cvpysdk.deployment.deploymentconstants import DownloadPackages, DownloadOptions
except ModuleNotFoundError:
    pass


def main():
    try:
        download_option_choices = [e.name for e in DownloadOptions]
        os_choices = [e.name for e in DownloadPackages]

        module_args = dict(
            download_option=dict(type=str, required=False, choices=download_option_choices, default=None),
            os_list=dict(type=list, required=False, choices=os_choices, default=None),
            service_pack=dict(type=int, required=False, default=None), 
            cu_number=dict(type=int, required=False, default=0),
            sync_cache=dict(type=bool, required=False, default=True),
            wait_for_job_completion=dict(type=bool, required=False, default=True)
        )
                        
        module = CVAnsibleModule(argument_spec=module_args)

        final_download_decision=os_to_download=None

        download_option= module.params['download_option']
        os_list = module.params['os_list']
        service_pack = module.params['service_pack']
        cu_number = module.params['cu_number']
        sync_cache = module.params['sync_cache']
        wait_for_job_completion = module.params['wait_for_job_completion']

        if download_option is not None:
            try:
                final_download_decision = DownloadOptions[download_option].value
            
            except KeyError:
                final_download_decision = DownloadOptions.LATEST_SERVICEPACK.value
        
        # If the value for Download Option is None/Incorrect; Default to Download Latest Service-Pack
        if download_option is None or final_download_decision is None:
            final_download_decision = DownloadOptions.LATEST_SERVICEPACK.value

        if final_download_decision == DownloadOptions.LATEST_SERVICEPACK.value or final_download_decision == DownloadOptions.LATEST_HOTFIXES.value:
            service_pack=None
            cu_number=0
        
        if final_download_decision == DownloadOptions.SERVICEPACK_AND_HOTFIXES.value:
            if service_pack is None:
                raise Exception("SP Number not appropriate to download a specific Service-Pack")

        if os_list is not None:
            os_to_download=[]
            for os in os_list:
                try:
                    os_to_download.append(DownloadPackages[os].value)
                
                except KeyError:
                    raise Exception("Please provide Correct/Appropriate value for the OS: " + str(os))

        download_job = module.commcell.download_software(options=final_download_decision,
                                                         os_list=os_to_download,
                                                         service_pack=service_pack,
                                                         cu_number=cu_number,
                                                         sync_cache=sync_cache)
        
        job_id = download_job.job_id
        module.result['job_id'] = str(job_id)

        if wait_for_job_completion:
            if not download_job.wait_for_completion():
                module.result['failed'] = True
                job_status = download_job.delay_reason
                raise Exception(str(job_status))
        
        module.result['failed'] = False
        module.result['changed'] = False
        module.exit_json(**module.result)

    except Exception as exp:
        module.result['failed'] = True
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()