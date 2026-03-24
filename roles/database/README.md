# Ansible Database Role - commvault.ansible.database
=========

Documentation  for the Role "Database".

## Requirements
------------

- Python 3 and above
- Install the `cvpysdk <https://pypi.org/project/cvpysdk/>`_ Commvault SDK for Python
- Commvault Software v11 SP26 or later release with WebConsole installed
- Commvault Ansible Modules: login, logout, job/wait_for_task_completion, database/backup, database/restore

## Role Variables
--------------

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
var_client  |  yes  |  | | The name of the client. | 
var_instance  |  yes  |  | | The name of the Instance. | 
var_agent_type  |  yes  |    | <ul> <li>sql server</li> <li>oracle</li><li>mysql</li><li>postgresql</li> </ul>  |  Agent Type.  | 
var_backupset  |   no  |  default backupset  | |  The name of the backupset. | 
var_subclient  |   no  |  subclient named 'default'.  | |  The name of the subclient. | 
var_backup_level  |  no  |  Full  |  <ul> <li>Full</li> <li>Incremental</li> <li>Differential</li> <li>Synthetic_full</li> </ul>  |  Backup Level.  |
var_content  |   no  |  | |  The database name(s) of the content that needs to be restored. | 
var_from_date  |  no  |  1979-01-26 08:00:16  | | The from date you want to restore database(format : YYYY-MM-DD HH:MM:SS ). | 
var_to_date  |  no  |  | | The to date you want to restore database (format : YYYY-MM-DD HH:MM:SS ). | 
var_in_place  |   no  |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  Whether the content needs to be restored in place i.e. restored back to the source location. | 
var_destination_client  |  no  |  | |  Destination client name in case the content needs to be restored to another location. | 
var_destination_instance  |   no  |  | |  Destination instance name in case the content needs to be restored to another location. | 
var_commvault_timeout  |   yes  |  | |  Time for timeout |
var_staging  |  no  |    |  | The staging path  |
var_restore_path  |  no  |  |  | List of dicts for restore paths of database files. |






#### Example Playbook 'backup_database.yml'
----------------

```
- hosts: localhost
  name: sample
  tasks:
    - name: Database Role
      import_roles:
        name: commvault.ansible.database
      vars:
        webserver_hostname: "demo_Name"
        commcell_username: "commcell_user"
        commcell_password: "commcell_password"
        var_client: "client_name"
        var_instance: "instance_name"
        var_agent_type: "agent_name"
        var_commvault_timeout: 300

```

Run playbook: ``` ansible-playbook backup_database.yml -t backup   ```

#### Example Playbook 'restore_database.yml'
----------------
```
- hosts: localhost
  name: sample
  tasks:
    - name: Database Role
      import_roles:
        name: commvault.ansible.database
      vars:
        webserver_hostname: "demo_Name"
        commcell_username: "commcell_user"
        commcell_password: "commcell_password"
        var_client: "client_name"
        var_instance: "instance_name"
        var_agent_type: "agent_name"
        var_staging: "/path/to/staging"
        var_restore_path:
          - "|DB1|#12!DB1_rename|#12!DB1|#12!E:RestoreLocationDB1.mdf|#12!C:Program FilesMicrosoft SQL ServerMSSQL10_50.MSSQLSERVERMSSQLDATADB1.mdf"
          - "|DB1|#12!DB1_rename|#12!DB1_log|#12!E:RestoreLocationDB1_log.ldf|#12!C:Program FilesMicrosoft SQL ServerMSSQL10_50.MSSQLSERVERMSSQLDATADB1_log.ldf"
        var_to_date: "2025/05/16 08:00:00"
        var_commvault_timeout: 300
```

Run playbook: ```ansible-playbook restore_database.yml -t restore ```

---

License
-------
 Copyright Commvault Systems, Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.



Author Information
------------------

