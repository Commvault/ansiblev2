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
module: commvault.ansible.workflow.export
short_description: Exports the workflow to the directory location specified by the user.
description: 
    - Exports the workflow XML to the directory location specified by the user.
    - commvault.ansible.workflow.export module can be used in playbooks to export the workflow to the directory location specified by the user.

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

    export_location:
        description:
            - Directory where the workflow would be exported
        type: str
        required: True

    
'''

EXAMPLES = '''
# Exports the workflow to the directory location specified by the user.

- name: "EXPORT_WORKFLOW"
  commvault.ansible.workflow.export:
    workflow_name: "Demo_CheckReadiness"
    export_location: "C:\TempDir"

- name: "EXPORT_WORKFLOW"
  commvault.ansible.workflow.export:
    workflow_name: "client check readiness"
    export_location: "C:\TempDir"

- name: "EXPORT_WORKFLOW"
  commvault.ansible.workflow.export:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    workflow_name: "client check readiness"
    export_location: "C:\TempDir"

'''

RETURN = r'''#'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():

    try:
        module_args =  dict(workflow_name=dict(type=str, required=True),
                            export_location=dict(type=str, required=True))

        module = CVAnsibleModule(argument_spec=module_args)

        workflow_name = module.params['workflow_name']
        export_location = module.params['export_location']
        workflow_instance=all_workflows=None

        if workflow_name is None:
            raise Exception("Please provide an appropriate WorkFlow Name")

        all_workflows = module.commcell.workflows
        all_workflows.refresh()

        if all_workflows.has_workflow(workflow_name):
            workflow_instance = all_workflows.get(workflow_name)

        else:
            raise Exception("Workflow not found on commcell, Please provide a Valid Workflow Name")

        exported_xml_path = workflow_instance.export_workflow(export_location=export_location)

        if exported_xml_path is None:
            module.result['failed'] = True
            raise Exception("Export Task Failed")

        module.result['failed'] = False        
        module.result['changed'] = False
        module.exit_json(**module.result)

    except Exception as exp:
        module.result['failed'] = True
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()