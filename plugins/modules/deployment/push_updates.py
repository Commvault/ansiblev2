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
module: commvault.ansible.deployment.push_updates
short_description: To Push Updates to the Clients from Commserver
description: 
    - This module pushes latest Updates to client from CommCell 
    - commvault.ansible.deployment.push_updates module can be used in playbooks to perform Push Updates to Clients

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

    client_names:
        description:
            - List of Client Names(Name on Commcell) to install service pack on
        type: list
        required: false
        default: None

    client_group_names:
        description:
            - list of Client groups to install service pack on
        type: list
        required: false
        default: None
    
    update_all_client_computers:
        description:
            -  boolean to specify whether to install on all clients
        type: bool
        required: false
        default: False

    update_all_client_computer_groups:
        description:
            -  boolean to specify whether to install on all clients groups
        type: bool
        required: false
        default: False
    
    reboot_client:
        description:
            - boolean to specify whether to reboot the client or not while installing updates
        type: bool
        required: false
        default: False

    run_db_maintenance:
        description:
            - boolean to specify whether to run rb maintenance or not
        type: bool
        required: false
        default: True

    install_maintenance_release_only:
        description:
            - boolean to specify whether to install only Maintenance Release or Not
        type: bool
        required: false
        default: False

    wait_for_job_completion:
        description:
            - Will wait for Download Job to Complete
        type: bool
        required: false
        default: True
'''

EXAMPLES = '''
# Run a File System Backup for default subclient of default backupset.

- name: "PUSH_UPDATES_TO_ALL_THE_CLIENTS"
  commvault.ansible.deployment.push_updates:
    update_all_client_computers: True
    reboot_client: False
    wait_for_job_completion: False

- name: "PUSH_UPDATES_TO_ALL_CLIENT_GROUPS"
  commvault.ansible.deployment.push_updates:
    client_names: 
      - clientname1
      - clientname2
    update_all_client_computers: True
    reboot_client: False

- name: "PUSH_UPDATES"
  commvault.ansible.deployment.push_updates:
    client_names: 
      - clientname1
      - clientname2
    client_group_names:
      - clientgroupname1
      - client_group_name2
    update_all_client_computers: False
    update_all_client_computer_groups: True
    reboot_client: False
    wait_for_job_completion: True

- name: "PUSH_UPDATES"
  commvault.ansible.deployment.push_updates:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    client_names: 
      - clientname1
      - clientname2
    client_group_names:
      - clientgroupname1
      - client_group_name2
    update_all_client_computers: False
    update_all_client_computer_groups: True
    reboot_client: False

'''

RETURN = r'''
job_id:
    description: Push Updates Job ID
    returned: success
    type: str
    sample: '2016'

'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule


def main():

    try:
        module_args =  dict(client_names=dict(type=list, required=False, default=None),
                            client_group_names=dict(type=list, required=False, default=None),
                            update_all_client_computers=dict(type=bool, required=False, default=False),
                            update_all_client_computer_groups=dict(type=bool, required=False, default=False),
                            reboot_client=dict(type=bool, required=False, default=False),
                            run_db_maintenance=dict(type=bool, required=False, default=True),
                            install_maintenance_release_only=dict(type=bool, required=False, default=False),
                            wait_for_job_completion=dict(type=bool, required=False, default=True)
                        )
                        
        module = CVAnsibleModule(argument_spec=module_args)

        client_computers = module.params['client_names']
        client_computer_groups = module.params['client_group_names']
        update_all_client_computers = module.params['update_all_client_computers']
        update_all_client_computer_groups = module.params['update_all_client_computer_groups']
        wait_for_job_completion = module.params['wait_for_job_completion']


        if not any([update_all_client_computers,
                    update_all_client_computer_groups,
                    client_computers,
                    client_computer_groups]):
            raise Exception("Please provide atleast one client or client group to be updated")

        reboot_client =  module.params['reboot_client']
        run_db_maintenance = module.params['run_db_maintenance']
        maintenance_release_only = module.params['install_maintenance_release_only']

        push_job = module.commcell.push_servicepack_and_hotfix(client_computers=client_computers,
                                                               client_computer_groups=client_computer_groups,
                                                               all_client_computers=update_all_client_computers,
                                                               all_client_computer_groups=update_all_client_computer_groups,
                                                               reboot_client=reboot_client,
                                                               run_db_maintenance=run_db_maintenance,
                                                               maintenance_release_only=maintenance_release_only)

        job_id = push_job.job_id
        module.result['job_id'] = str(job_id)

        if wait_for_job_completion:
            if not push_job.wait_for_completion():
                module.result['failed'] = True
                job_status = push_job.delay_reason
                raise Exception(str(job_status))
        
        module.result['failed'] = False
        module.result['changed'] = False
        module.exit_json(**module.result)

    except Exception as exp:
        module.result['failed'] = True
        module.fail_json(msg=str(exp), changed=False)


if __name__ == "__main__":
    main()