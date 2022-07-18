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
module: commvault.ansible.job.status
short_description: Checks the status of the Job
description: 
    - This module Checks the Job Status
    - commvault.ansible.job.status module can be used in playbooks to check the job status

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

    wait_for_job_completion:
        description:
            - wait till job status is changed to Completed/Failed
        type: bool
        required: false
        default: false

'''

EXAMPLES = '''
# Checks the status of the particular Job

- name: "Job Status"
  commvault.ansible.job.status:
    job_id: 3

- name: "Job Status"
  commvault.ansible.job.status:
    job_id: 7
    wait_for_job_completion: False

- name: "Wait for Job Completion and provide the Job Status"
  commvault.ansible.job.status:
    job_id: 18
    wait_for_job_completion: True

- name: "Job Status"
  commvault.ansible.job.status:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    job_id: 23

'''

RETURN = r'''
job_id:
    description: Status of the Job 
    type: str 
    sample: 'Running/Completed'

'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule
try:
    from cvpysdk.job import Job
    from cvpysdk.exception import SDKException
except ModuleNotFoundError:
    pass


def main():
    try:
        module_args = dict(job_id=dict(type=int, required=True),
                           wait_for_job_completion=dict(type=bool, required=False, default=False))
                        
        module = CVAnsibleModule(argument_spec=module_args)

        job_id = int(module.params['job_id'])
        wait_for_job_completion = module.params['wait_for_job_completion']
        commcell_obj = module.commcell

        job_instance = Job(commcell_object=commcell_obj, job_id=job_id)

        if wait_for_job_completion:
            job_instance.wait_for_completion()

        job_status=job_instance.summary['status']
        module.result["job_status"]=job_status

        module.result['failed'] = False
        module.result['changed'] = False
        module.exit_json(**module.result)

    except Exception as exp:
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()