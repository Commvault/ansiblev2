# Ansible FS Deployment Role - commvault.ansible.fs_deployment

Documentation for the Role "File System Deployment".

---
## Requirements

- Python 3 and above
- Install the `cvpysdk <https://pypi.org/project/cvpysdk/>`_ Commvault SDK for Python
- Commvault Software v11 SP26 or later release with WebConsole installed
- Commvault Ansible Modules: Login, Deployment, Backup

## Role Variables

| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
os_type  |  yes  |  | <ul> <li>windows</li>  <li>unix</li>  |  Operating System type  |
client_computers  |   yes  |  | |  Hostname of the computers to push File System Package |
windows_package  |   no  |  FILE_SYSTEM  | <ul> <li>ACTIVE_DIRECTORY</li>  <li>CLOUD_APPS</li>  <li>DOMINO_DATABASE</li>  <li>EXCHANGE</li>  <li>FILE_SYSTEM</li>  <li>MEDIA_AGENT</li>  <li>SHAREPOINT</li>  <li>ORACLE</li>  <li>POSTGRESQL</li>  <li>SQLSERVER</li>  <li>VIRTUAL_SERVER</li>  <li>VSS_PROVIDER</li>  <li>WEB_CONSOLE</li>  <li>TEST_AUTOMATION</li>  <li>PYTHON_SDK</li>  <li>COMMSERVE_LITE</li>  <li>CONTENT_ANALYZER</li> </ul> |  list of windows features to be installed | 
unix_packages  |   no  |  FILE_SYSTEM  | <ul> <li>CASSANDRA</li>  <li>CLOUD_APPS</li>  <li>DOMINO_DATABASE</li>  <li>FILE_SYSTEM</li>  <li>FILE_SYSTEM_FOR_IBMI</li>  <li>FILE_SYSTEM_FOR_OPEN_VMS</li>  <li>MEDIA_AGENT</li>  <li>ORACLE</li>  <li>POSTGRESQL</li>  <li>SAPHANA</li>  <li>SQLSERVER</li>  <li>VIRTUAL_SERVER</li>  <li>TEST_AUTOMATION</li>  <li>PYTHON_SDK</li>  <li>CONTENT_ANALYZER</li> </ul> |  list of unix features to be installed |
username  |   yes  |  | |  Username of the client machine to install features on |
password  |   yes  |  | |  Password of the client machine to install features on |
client_group_name  |   no  |  | |  List of the client groups for the client |
storage_policy_name  |   no  |  | | Storage policy for the default subclient |
sw_cache_client  |   no  |  | | Remote Cache Client Name/ Over-riding Software Cache |
install_path  |   no  |  | | Install to a specified path on the client |
plan  |  yes  |  | | The name of the server plan which needs to be associated to the entity |
backupset  |  no  |  | |  The name of the backupset. | 
subclient  |   no  |  | |  The name of the subclient. | 

#### Example Playbook

```
- hosts: localhost
  name: Roles Testing
  tasks:
    - name: FS Role
      import_role:
        name: commvault.ansible.fs_deployment
      vars:
        os_type: "windows"
        webserver_hostname: "demo-CS-Name"
        commcell_username: "commcell_user"
        commcell_password: "commcell_password"
        client_computers:
          - democs.example.com
          - x.x.x.x
        username: "machine-username"
        password: "machine-password"
        client_group_name:
          - random_group1
          - random_group2
          - random_group3
        storage_policy_name: "policy_name"
        install_path: "D:\\Random"
        sw_cache_client: "client_name"
        plan: "plan_name1"
        subclient:  "subclient_name1"

```





















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
Commvault Systems, Inc.