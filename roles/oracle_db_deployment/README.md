# Ansible Oracle DB Deployment Role - commvault.ansible.oracle_db_deployment

Documentation for the Role "Oracle DB Deployment" on Linux.
For other database deployments, the componentID in file 'addServer.yml' needs to be changed.

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
commcell_username  |   no  |  | |  Commcell Username | 
commcell_password  |   no  |  | |  Commcell Password | 
var_storageName  |   yes  |  | |  Storage name |
var_mediaAgent  |   yes  |  | |  MediaAgent to create storage on |
var_mountPath  |   yes  |  | |  Mount path of storage |
var_deduplicationDBPath  |   yes  |  | |  DDB path for storage |
var_plan  |   yes  |  | |  New plan name for DB instance |
var_clientName  |   yes  |  | |  Client machine name |
var_dbInst  |   yes  |  | |  DB Instance |
var_dbUser  |   yes  |  | |  DB Username |
var_dbPwd  |   yes  |  | |  DB Password |
var_dbPwd2  |   no  |  | |  DB base64 Password  |
var_dbHome  |   yes  |  | |  DB Home |
var_osUser  |   yes  |  | |  OS Username |
var_osPwd  | yes |  | |  OS User Password |
var_osPwd2 | no |  | |  OS base64 Password |



#### Example Playbook 'db_role.yml'

```
- name: sample
  hosts: localhost
  remote_user: root
  become: true

  tasks:
    - name: "DB Role"
      import_role:
        name: commvault.ansible.oracle_db_deployment
      vars:
        webserver_hostname: 'hostname.location' 
        commcell_username: 'username'
        commcell_password: 'password'
        var_storageName: 'store1'
        var_mediaAgent: 'ma1'
        var_mountPath: "E:\\store"
        var_deduplicationDBPath: "E:\\ddb"
        var_plan: 'plan1'
        var_clientName: 'ora'
        var_dbInst: 'ORCL'
        var_dbUser: 'sys'
        var_dbPwd: 'password'
        var_dbPwd2: "{{ var_dbPwd|b64encode }}"
        var_dbRePwd: "{{ var_dbPwd2|b64encode }}"    
        var_dbHome: "E:\\db"
        var_osUser: "oracle"
        var_osPwd: "ospwd"
        var_osPwd2: "{{ var_osPwd|b64encode }}"
		
      register: response
    - debug:
        msg: "{{ response }}"

```

Run playbook by including ```ANSIBLE_JINJA_NATIVE=True```
```ANSIBLE_JINJA_NATIVE=True ansible-playbook -vvv db_role.yml```



















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