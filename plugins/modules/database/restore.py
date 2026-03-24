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
---
module: commvault.ansible.database.restore
short_description: to perform restore of a database subclient.
description:
    - commvault.ansible.database.restore can be used to perform a database restore operation.

options:
    webserver_hostname:
        description:
            - Hostname of the Web Server.
        type: str
        required: false
    commcell_username:
        description:
            - Commcell username
        type: str
        required: false
    commcell_password:
        description:
            - Commcell password
        type: str
        required: false
    client:
        description:
            - The name of the Client.
        type: str
        required: true
    instance:
        description:
            - The name of the Instance.
        type: str
        required: true
    agent_type:
        description:
            - The agent type.
        type: str
        required: true
        default: None
        choices: ["sql server","oracle","mysql", "postgresql"]
    backupset:
        description:
            - The name of the backupset.
        type: str
        required: false
        default: default backupset.
    subclient:
        description:
            - The name of the subclient.
        type: str
        required: false
        default: subclient name default.
    content:
        description:
            - The name of the database that needs to be restored.
        type: str
        required: false
        default: None
    from_date:
        description:
            - the date from restore.
        format: 'YYYY-MM-DD HH:MM:SS'
        type: str
        required: false
        default: "1979-01-26 08:00:16"
    to_date:
        description:
            - the date to restore.
        format: 'YYYY-MM-DD HH:MM:SS'
        type: str
        required: false
        default: None
    in_place:
        description:
            -  Whether the database needs to be restored in place i.e. restored back to the source location.
        type: bool
        required: false
        default: True
    destination_client:
        description:
            - Destination client name in case the database needs to be restored to another location.
        type: str
        required: false
        default: None
    destination_instance:
        description:
            - Destination instance name in case the database needs to be restored to another location.
        type: str
        required: false
        default: None
    staging:
        description:
            - Staging path for the  mysql database restore operation.
        type: str
        required: false
        default: None
    restore_path:
        description:
            -  List of dicts for restore paths of database files.
        type: list
        required: false
        default: None

'''

EXAMPLES = r'''
- name: Run a Database Restore for default subclient of default backupset with agent_type of 'mysql', session file will be used.
  commvault.ansible.database.restore:
   client: "client_name"
   instance: "instance_name"

- name: Run a Database Restore for subclient for subclient 'user_subclient' of backupset 'user_backupset' with agent_type of 'mysql', session file will be used.
  commvault.ansible.database.restore:
   client: "client_name"
   instance: "instance_name"
   backupset: "user_backupset"
   subclient: "user_subclient"
   agent_type: "mysql"
   content: "/database_name"

- name: Run a Database Restore for default subclient of default backupset with agent_type of 'mysql' and to date '2025/05/16 08:00:00', session file will be used.
  commvault.ansible.database.restore:
    client: "client_name"
    instance: "instance_name"
    agent_type: "mysql
    to_date: "2025/05/16 08:00:00"

- name: Run a Database Restore out of place for default subclient of default backupset with agent_type of 'mysql' and to date '2025/05/16 08:00:00', session file will be used.
  commvault.ansible.database.restore:
    client: "client_name"
    instance: "instance_name"
    agent_type: "mysql
    in_place: false
    destination_client: "destination_client_name"
    destination_instance: "destination_instance_name"

- name: Run a Database Restore out of place for default subclient of default backupset with agent_type of 'mysql', session file will be used.
  commvault.ansible.database.restore:
    client: "client_name"
    instance: "instance_name"
    agent_type: "mysql
    to_date: "2025/05/16 08:00:00"
    in_place: false
    destination_client: "destination_client_name"
    destination_instance: "destination_instance_name"

- name: Run a Database Restore with staging path for default subclient of default backupset, session file will be used.
  commvault.ansible.database.restore:
    client: "client_name"
    instance: "instance_name"
    agent_type: "mysql"
    content: "/database_name"
    staging: "/path/to/staging"

- name: Run a Database Restore out of place for default subclient of default backupset with log path and data path specify, session file will be used.
  commvault.ansible.database.restore:
    client: "client_name"
    instance: "instance_name"
    agent_type: "sql server"
    content: "/database_name"
    destination_instance: "destination_instance"
    restore_path:
      - "|original_database_name|#12!restore_database_name|#12!logical_file_name|#12!restore_file_path_with_file_names|#12!original_file_path_with_file_names"
      - "|DB1|#12!DB1_rename|#12!DB1|#12!E:RestoreLocationDB1.mdf|#12!C:Program FilesMicrosoft SQL ServerMSSQL10_50.MSSQLSERVERMSSQLDATADB1.mdf"
      - "|DB1|#12!DB1_rename|#12!DB1_log|#12!E:RestoreLocationDB1_log.ldf|#12!C:Program FilesMicrosoft SQL ServerMSSQL10_50.MSSQLSERVERMSSQLDATADB1_log.ldf"
'''

RETURN = r'''
job_id:
    description: Restore job ID
    returned: On success
    type: str
    sample: '2025'
'''

from datetime import datetime
from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule

def main ():
    """Main method for this module."""

    module_args = dict(
        client=dict(type=str, required=True),
        backupset=dict(type=str, required=False),
        subclient=dict(type=str, required=False),
        agent_type=dict(type=str, required=True),
        instance = dict(type=str, required=True),
        from_date = dict(type=str, required=False),
        content = dict(type=str, required=True),
        to_date = dict(type=str, required=False),
        destination_client = dict(type= str, required=False),
        destination_instance = dict(type=str, required= False),
        in_place = dict(type=bool, required=False, default=True),
        staging = dict(type=str, required=False),
        restore_path = dict(type=list, required=False)
    )

    module = CVAnsibleModule(argument_spec=module_args)
    module.result['changed'] = False

    try:
        client = module.commcell.clients.get(module.params.get('client'))
        agent_type = module.params.get('agent_type', '').lower()
        agent = client.agents.get(agent_type)
        instance = agent.instances.get(module.params.get('instance'))
        backupset = instance.backupsets.get(agent.backupsets.default_backup_set if not module.params.get('backupset') else module.params.get('backupset'))
        subclient = backupset.subclients.get(backupset.subclients.default_subclient if not module.params.get('subclient') else module.params.get('subclient'))
        content = module.params.get('content','')
        from_date = module.params.get('from_date','1979-01-26 08:00:16')
        to_date = module.params.get('to_date','')
        destination_client = module.params.get('destination_client','' )
        destination_instance = module.params.get('destination_instance','')
        staging = module.params.get('staging','')
        restore_path = module.params.get('restore_path',[])
        in_place = module.params.get('in_place', True)
        from_time_convert = ''
        to_time_convert = ''

        if to_date :
            date_to =  datetime.strptime(to_date, '%Y-%m-%d %H:%M:%S')
            to_time_convert = int(date_to.timestamp())
            date_from =datetime.strptime(from_date, '%Y-%m-%d %H:%M:%S')
            from_time_convert = int(date_from.timestamp())

        if not destination_instance and not destination_client:
            in_place = True
        else :
            in_place = False

        use_staging = staging and staging.strip() !=''
        restore = ''

        if not use_staging :

            match (content, to_date,in_place, agent_type):

                case _ if not content  and not to_date and in_place is True :
                    browse_content = instance.browse()
                    content = browse_content[0]
                    restore = subclient.restore_in_place(paths=content)

                case _ if not content  and to_date and in_place is True :
                    browse_content = instance.browse(from_time= from_date,
                                                        to_time = to_date)
                    content = browse_content[0]
                    restore = subclient.restore_in_place(paths=content,
                                                            from_time=from_time_convert ,
                                                            to_time=to_time_convert )

                case _ if content and not to_date and in_place is True :
                    restore = subclient.restore_in_place(paths=[content])

                case _ if content  and to_date and in_place is True :
                    restore = subclient.restore_in_place(paths=[content],
                                                            from_time= from_time_convert,
                                                            to_time= to_time_convert )

                case _ if  not content  and not to_date and in_place is False and agent_type == 'sql server':
                    browse_content = instance.browse()
                    content = browse_content[0]
                    restore = instance.restore(content_to_restore=content,
                                                destination_instance=destination_instance,
                                                restore_path=restore_path)

                case _ if not content  and to_date and in_place is False and agent_type == 'sql server':
                    browse_content = instance.browse(from_time= from_date,
                                                        to_time = to_date)
                    content = browse_content[0]
                    restore = instance.restore(content_to_restore=content,
                                                destination_instance=destination_instance,
                                                to_time=to_time_convert,
                                                restore_path=restore_path)

                case _ if content and not to_date and in_place is False and agent_type == 'sql server':
                    restore = instance.restore(content_to_restore=[content],
                                                destination_instance=destination_instance,
                                                restore_path=restore_path)

                case _ if content  and to_date and in_place is False and agent_type == 'sql server':
                    restore = instance.restore(content_to_restore=[content],
                                                destination_instance=destination_instance,
                                                to_time= to_time_convert,
                                                restore_path=restore_path)

                case _ if  not content  and not to_date and in_place is False:
                    browse_content = instance.browse()
                    content = browse_content[0]
                    restore = subclient.restore_out_of_place(client=destination_client,
                                                            destination_path=destination_instance,
                                                            paths=content)

                case _ if not content  and to_date and in_place is False:
                    browse_content = instance.browse(from_time= from_date,
                                                        to_time = to_date)
                    content = browse_content[0]
                    restore = subclient.restore_out_of_place(client=destination_client,
                                                            destination_path=destination_instance,
                                                            paths=content,
                                                            from_time=from_time_convert ,
                                                            to_time=to_time_convert )

                case _ if content and not to_date and in_place is False:
                    restore = subclient.restore_out_of_place(client=destination_client,
                                                            destination_path=destination_instance,
                                                            paths=[content])

                case _ if content  and to_date and in_place is False:
                    restore = subclient.restore_out_of_place(client=destination_client,
                                                            destination_path=destination_instance,
                                                            paths=[content],
                                                            from_time= from_time_convert,
                                                            to_time= to_time_convert )
        else :
            match (content, to_date,in_place, agent_type):

                case _ if not content  and not to_date and in_place is True and agent_type == 'mysql':
                    browse_content = instance.browse()
                    content = browse_content[0]
                    restore = instance.restore_in_place(
                        paths=content,
                        staging= staging)

                case _ if not content  and to_date and in_place is True and agent_type == 'mysql' :
                    browse_content = instance.browse(from_time= from_date,
                                                        to_time = to_date)
                    content = browse_content[0]
                    restore = instance.restore_in_place(paths=content,
                                                            staging=staging,
                                                            from_time=from_time_convert ,
                                                            to_time=to_time_convert )

                case _ if content and not to_date and in_place is True and agent_type == 'mysql' :
                    restore = instance.restore_in_place(paths=[content],
                                                        staging=staging)

                case _ if content  and to_date and in_place is True and agent_type == 'mysql' :
                    restore = instance.restore_in_place(paths=[content],
                                                            staging=staging,
                                                            from_time= from_time_convert,
                                                            to_time= to_time_convert )

                case _ if  not content  and not to_date and in_place is False and agent_type == 'mysql' :
                    browse_content = instance.browse()
                    content = browse_content[0]
                    restore = instance.restore_out_of_place(client=destination_client,
                                                            staging=staging,
                                                            paths=content,
                                                            destination_path=destination_instance,)

                case _ if not content  and to_date and in_place is False and agent_type == 'mysql' :
                    browse_content = instance.browse(from_time= from_date,
                                                        to_time = to_date)
                    content = browse_content[0]
                    restore = instance.restore_out_of_place(paths=content,
                                                            staging=staging,
                                                            client=destination_client,
                                                            destination_path=destination_instance,
                                                            from_time=from_time_convert ,
                                                            to_time=to_time_convert )

                case _ if content and not to_date and in_place is False and agent_type == 'mysql' :
                    restore = instance.restore_out_of_place(paths=[content],
                                                             staging=staging,
                                                             client=destination_client,
                                                            destination_path=destination_instance,
                                                            )

                case _ if content  and to_date and in_place is False and agent_type == 'mysql' :
                    restore = instance.restore_out_of_place(paths=[content],
                                                            staging=staging,
                                                            client=destination_client,
                                                            destination_path=destination_instance,
                                                            from_time= from_time_convert,
                                                            to_time= to_time_convert )

        module.result['job_id'] = str(restore.job_id)
        module.result['changed'] = True
        module.result['status'] = str(restore.status)

        module.exit_json(**module.result)

    except Exception as e:
        module.result['msg'] = str(e)
        module.fail_json(**module.result)


if __name__ == '__main__':
    main()
