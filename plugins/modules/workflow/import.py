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


from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule
DOCUMENTATION = '''
module: commvault.ansible.workflow.import
short_description: Imports a workflow to the Commcell.
description: 
    - Imports a workflow to the Commcell.
    - commvault.ansible.workflow.import module can be used in playbooks to import a workflow on the Commcell.

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

    workflow_xml_path:
        description:
            - path of the workflow xml file / XMl contents
        type: str
        required: True

    
'''

EXAMPLES = '''
# Imports a workflow to the Commcell.

- name: "IMPORT_WORKFLOW"
  commvault.ansible.workflow.import:
    workflow_xml_path:  "C:\TempDir"

- name: "IMPORT_WORKFLOW"
  commvault.ansible.workflow.import:
    workflow_xml_path:  "C:\TempDir"

- name: "IMPORT_WORKFLOW"
  commvault.ansible.workflow.import:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    workflow_xml_path:  "C:\TempDir"

'''

RETURN = r'''#'''


def main():

    try:
        module_args = dict(workflow_xml_path=dict(type=str, required=True))

        module = CVAnsibleModule(argument_spec=module_args)

        workflow_xml_path = module.params['workflow_xml_path']

        all_workflows = module.commcell.workflows
        all_workflows.refresh()

        all_workflows.import_workflow(workflow_xml=workflow_xml_path)

        module.result['failed'] = False
        module.result['changed'] = False
        module.exit_json(**module.result)

    except Exception as exp:
        module.result['failed'] = True
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()