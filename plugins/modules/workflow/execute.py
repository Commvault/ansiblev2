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
module: commvault.ansible.workflow.execute
short_description: Executes the workflow with the workflow name and inputs
description: 
    - This module executes the given Workflow along with it's inputs
    - commvault.ansible.workflow.execute module can be used in playbooks to execute the Workflows on client from Commcell

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

    workflow_name:
        description:
            - Name of the Workflow 
        type: str
        required: true

    workflow_inputs:
        description:
            - Dictionary consisting of inputs to execute the workflow
        type: dict
        required: True
    
    hidden_workflow:
        description:
            - Is the workflow hidden ?
        type: bool
        required: false
        default: False

    
'''

EXAMPLES = '''
# Executes the workflow on given Clients/ClientGroups with the workflow name as inputs

- name: "EXECUTE_WORKFLOW"
  commvault.ansible.workflow.execute:
    workflow_name: "Demo_CheckReadiness"
    workflow_inputs: 
        ClientGroupName: "client_group1"

- name: "EXECUTE_WORKFLOW"
  commvault.ansible.workflow.execute:
    workflow_name: "client check readiness"
    workflow_inputs: 
        input1_name: "input1_value"
        input2_name: "input2_value"
    hidden: True
    wait_for_job_completion: False

- name: "EXECUTE_WORKFLOW"
  commvault.ansible.workflow.execute:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    workflow_name: "client check readiness"
    workflow_inputs: 
        input1_name: "input1_value"
        input2_name: "input2_value"
    hidden: True

'''

RETURN = r'''
job_id:
    description: Relevant workflow job ID (-1 if N/A)
    returned: success
    type: str 
    sample: '2016'

'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule
try:
    from cvpysdk.job import Job
except ModuleNotFoundError:
    pass

def main():

    try:
        module_args =  dict(workflow_name=dict(type=str, required=True),
                            workflow_inputs=dict(type=dict, required=False, default=None),
                            hidden_workflow=dict(type=bool, required=False, default=False),
                            wait_for_job_completion=dict(type=bool, required=False, default=True)
                            )

        module = CVAnsibleModule(argument_spec=module_args)

        workflow_name = module.params['workflow_name']
        workflow_inputs = module.params['workflow_inputs']
        hidden_workflow =  module.params['hidden_workflow']
        wait_for_job_completion = module.params['wait_for_job_completion']

        workflow_instance=all_workflows=None

        if workflow_name is None:
            raise Exception("Please provide an appropriate WorkFlow Name")

        all_workflows = module.commcell.workflows
        all_workflows.refresh()

        if all_workflows.has_workflow(workflow_name):
            workflow_instance = all_workflows.get(workflow_name)

        else:
            raise Exception("Workflow not found on commcell, Please provide a Valid Workflow Name")

        _, workflow_job = workflow_instance.execute_workflow(workflow_inputs=workflow_inputs,
                                                          hidden=hidden_workflow)

        if isinstance(workflow_job, Job):
            job_id = workflow_job.job_id
            module.result['job_id'] = str(job_id)

            if wait_for_job_completion:
                if not workflow_job.wait_for_completion():
                    module.result['failed'] = True
                    job_status = workflow_job.delay_reason
                    raise Exception(str(job_status))
        else:
            module.result['job_id'] = -1
            module.result['status'] = workflow_job

        module.result['failed'] = False
        module.result['changed'] = False
        module.exit_json(**module.result)

    except Exception as exp:
        module.result['failed'] = True
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()