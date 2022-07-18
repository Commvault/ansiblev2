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
module: commvault.ansible.job.suspend
short_description: Suspends the Job
description: 
    - This module suspends the job
    - commvault.ansible.job.suspend module can be used in playbooks to suspend the job

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
    
    job_id:
        description:
            - ID of the job
        type: int
        required: True

    wait_for_job_to_suspend:
        description:
            - wait until job status is changed to Suspended
        type: bool
        required: false
        default: false

'''

EXAMPLES = '''
# Suspends a particular Job

- name: "Suspend Job"
  commvault.ansible.job.suspend:
    job_id: 3

- name: "Suspend Job"
  commvault.ansible.job.suspend:
    job_id: 7
    wait_for_job_to_suspend: False

- name: "Suspend Job and Wait for Suspend Task to be completed"
  commvault.ansible.job.suspend:
    job_id: 18
    wait_for_job_to_suspend: True

- name: "Suspend Job"
  commvault.ansible.job.suspend:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    job_id: 23

'''

RETURN = r'''#'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule
try:
    from cvpysdk.job import Job
    from cvpysdk.exception import SDKException
except ModuleNotFoundError:
    pass


def main():
    try:
        module_args = dict(job_id=dict(type=int, required=True),
                           wait_for_job_to_suspend=dict(type=bool, required=False, default=False))
                        
        module = CVAnsibleModule(argument_spec=module_args)

        job_id = int(module.params['job_id'])
        wait_for_job_to_suspend = module.params['wait_for_job_to_suspend']
        commcell_obj = module.commcell

        job_instance = Job(commcell_object=commcell_obj, job_id=job_id)
        job_instance.pause(wait_for_job_to_pause=wait_for_job_to_suspend)

        module.result['failed'] = False
        module.result['changed'] = True
        module.exit_json(**module.result)

    except Exception as exp:
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()