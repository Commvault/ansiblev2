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
module: commvault.ansible.workflow.deploy
short_description: Deploys a workflow on the Commcell.
description: 
    - Deploys a workflow on the Commcell.
    - commvault.ansible.workflow.deploy module can be used in playbooks to Deploys a workflow on the Commcell.

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

    workflow_engine:
        description:
            - name of the client to deploy the workflow on
        type: str
        required: True

    workflow_xml_path:
        description:
            - path of the workflow xml file / XMl contents
        type: str
        required: True

    
'''

EXAMPLES = '''
# Deploys a workflow on the Commcell.

- name: "DEPLOY_WORKFLOW"
  commvault.ansible.workflow.deploy:
    workflow_name: "Demo_CheckReadiness"
    workflow_engine:  "TempClient"
    workflow_xml_path:  "C:\TempDir"

- name: "DEPLOY_WORKFLOW"
  commvault.ansible.workflow.deploy:
    workflow_name: "client check readiness"
    workflow_engine:  "TempClient"
    workflow_xml_path:  "C:\TempDir"

- name: "DEPLOY_WORKFLOW"
  commvault.ansible.workflow.deploy:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    workflow_name: "client check readiness"
    workflow_engine:  "TempClient"
    workflow_xml_path:  "C:\TempDir"

'''

RETURN = r'''#'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():

    try:
        module_args =  dict(workflow_name=dict(type=str, required=True),
                            workflow_engine=dict(type=str, required=True),
                            workflow_xml_path=dict(type=str, required=True))

        module = CVAnsibleModule(argument_spec=module_args)

        workflow_name = module.params['workflow_name']
        workflow_engine = module.params['workflow_engine']
        workflow_xml_path = module.params['workflow_xml_path']
        workflow_instance=all_workflows=None

        if workflow_name is None:
            raise Exception("Please provide an appropriate WorkFlow Name")

        all_workflows = module.commcell.workflows
        all_workflows.refresh()

        if all_workflows.has_workflow(workflow_name):
            workflow_instance = all_workflows.get(workflow_name)

        else:
            raise Exception("Workflow not found on commcell, Please provide a Valid Workflow Name")

        workflow_instance.deploy_workflow(workflow_engine=workflow_engine,
                                          workflow_xml=workflow_xml_path)

        module.result['failed'] = False        
        module.result['changed'] = False
        module.exit_json(**module.result)

    except Exception as exp:
        module.result['failed'] = True
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()