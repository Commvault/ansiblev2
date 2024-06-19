# Ansible Collection - commvault.ansible
----
  * [Requirements](#require)
  * [Install Instructions](#install)
  * [Contribution Guidelines](#contrib)
  * [License](#license)
  * [About Commvault](#about)
  * [Additional Roles](#roles)
  * [Documentation](#docs)

## Requirements <a name="require"></a>
----
1. Ansible
2. Python 3.6+
3. [CVPySDK](https://github.com/Commvault/cvpysdk)
4. Commvault Software v11 SP16+ with Webconsole package installed

## Install Instructions <a name="install"></a>
----
Install ``cvpysdk`` using the ``requirements.txt`` file by running ``pip install -r requirements.txt``  

You can install this collection from the Ansible Galaxy using the command ``ansible-galaxy collection install commvault.ansible``  
You can also manually clone this repository in the given location ``<Default Ansible Collection Location>/ansible_collections/commvault/`` and rename the repo folder from ``ansiblev2`` to ``ansible`` to install this collection without using Ansible Galaxy

## Contribution Guidelines <a name="contrib"></a>
----
1. We welcome all the enhancements from everyone although we request the developer to follow some guidelines while interacting with the ``Commvault Ansible Collection`` codebase.
2. Before adding any enhancements/bug-fixes, we request you to open an Issue first.
3. The core team will go over the Issue and notify if it is required or already been worked on.
4. If the Issue is approved, the contributor can then make the changes to their fork and open a pull request.

 ### Coding Considerations
 - All python code should be **PEP8** compliant.
 - All changes should be consistent with the design of the SDK.
 - The code should be formatted using **autopep8** with line-length set to **119** instead of default **79**.
 - All changes and any new methods/classes should be properly documented.
 - The docstrings should be of the same format as existing docs.

 ### Code of Conduct

- Everyone interacting in the ``Commvault Ansible Collection`` project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [**PyPA Code of Conduct**](https://www.pypa.io/en/latest/code-of-conduct/).

## License <a name="license"></a>
----
``CVPySDK`` and ``Commvault Ansible Collection`` are licensed under [``Apache 2.0``](https://raw.githubusercontent.com/Commvault/ansiblev2/main/LICENSE)

## About Commvault <a name="about"></a>
----
![Commvault](https://commvault.github.io/cvpysdk/logo.png "Commvault")

[**Commvault**](https://www.commvault.com/) (NASDAQ: CVLT) is a publicly-traded data protection and information management software company headquartered in Tinton Falls, New Jersey.
It was formed in 1988 as a development group in Bell Labs, and later became a business unit of AT&T Network Systems. It was incorporated in 1996.
Commvault software assists organizations with data backup and recovery, cloud and infrastructure management, and retention and compliance.

## Additional Roles <a name="roles"></a>
[fs_deployment](roles/fs_deployment/README.md): For File System deployment  
[oracle_db_deployment](roles/oracle_db_deployment/README.md): For Oracle DB Deployment

## Documentation for the collection <a name="docs"></a>

---
### Modules


  * [commvault.ansible.login - login in to the commcell with provided credentials or auth token.](#commvault.ansible.login)

  * [commvault.ansible.logout - logs out of the commcell.](#commvault.ansible.logout)

  * [commvault.ansible.request - makes a http request on the commserver api](#commvault.ansible.request)

  * [commvault.ansible.deployment.install_software - to perform push installation from the commserve](#commvault.ansible.deployment.install_software)

  * [commvault.ansible.deployment.download_software - to perform download software on commserve](#commvault.ansible.deployment.download_software)

  * [commvault.ansible.deployment.push_updates - to push updates to the clients from commserver](#commvault.ansible.deployment.push_updates)

  * [commvault.ansible.file_servers.manage_content - to update the properties of a file server at subclient level.](#commvault.ansible.file_servers.manage_content)

  * [commvault.ansible.file_servers.backup - to perform backup of a file server subclient.](#commvault.ansible.file_servers.backup)

  * [commvault.ansible.file_servers.manage_plan - to change the plan associated to the client, backupset or subclient.](#commvault.ansible.file_servers.manage_plan)

  * [commvault.ansible.file_servers.restore - to perform restore of a file server subclient.](#commvault.ansible.file_servers.restore)

  * [commvault.ansible.job.kill - kills the job](#commvault.ansible.job.kill)

  * [commvault.ansible.job.resume - resumes the job](#commvault.ansible.job.resume)

  * [commvault.ansible.job.status - checks the status of the job](#commvault.ansible.job.status)

  * [commvault.ansible.job.suspend - suspends the job](#commvault.ansible.job.suspend)

  * [commvault.ansible.plans.add - creates a plan](#commvault.ansible.plans.add)

  * [commvault.ansible.plans.delete - deletes a plan](#commvault.ansible.plans.delete)

  * [commvault.ansible.workflow.execute - executes the workflow with the workflow name and inputs](#commvault.ansible.workflow.execute)

  * [commvault.ansible.workflow.deploy - deploys a workflow on the commcell.](#commvault.ansible.workflow.deploy)

  * [commvault.ansible.workflow.export - exports the workflow to the directory location specified by the user.](#commvault.ansible.workflow.export)

  * [commvault.ansible.workflow.import - imports a workflow to the commcell.](#commvault.ansible.workflow.import)

  * [commvault.ansible.storage.disk.detail - gets details of a disk storage](#commvault.ansible.storage.disk.detail)

  * [commvault.ansible.storage.disk.add - creates a disk storage](#commvault.ansible.storage.disk.add)


---


## commvault.ansible.login <a name="commvault.ansible.login"></a>
Login in to the Commcell with provided credentials or auth token.


#### Synopsis
 commvault.ansible.login can be used to login to Commcell using credentials or auth. token.












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   yes  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username. | 
commcell_password  |   no  |  | |  Commcell password. | 
auth_token  |   no  |  | |  A authentication token that can be used in place of commcell_username and commcell_password to login. | 
verify_ssl  |   no  | True | |  Verify the SSL certificate of the commcell. | 
certificate_path  |   no  |  | |  path of the CA_BUNDLE or directory with certificates of trusted CAs (including trusted self-signed certificates) | 














#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
authtoken |  On success  |   str  |   The authentication token  |   QSDK value_of_token  |




#### Examples

```
- name: Log in to the Commcell
  commvault.ansible.login:
    webserver_hostname: 'web_server_hostname' 
    commcell_username: 'user'
    commcell_password: 'password'

```





















---



## commvault.ansible.logout <a name="commvault.ansible.logout"></a>
Logs out of the Commcell.


#### Synopsis
 commvault.ansible.logout can be used to logout of the Commcell stored in the session file.

























#### Examples

```
- name: Log out of the Commcell
  commvault.ansible.logout:

```





















---



## commvault.ansible.request <a name="commvault.ansible.request"></a>
Makes a HTTP request on the Commserver API


#### Synopsis
 This module makes HTTP requests to the Commserver API












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
method  |   yes  |  | <ul> <li>GET</li>  <li>POST</li>  <li>PUT</li>  <li>DELETE</li> </ul> |  Web method to use to make the request | 
url  |   yes  |  | |  The web URL or service to run the HTTP request on. Use "{0}" to autopopulate webconsole URL | 
payload  |   no  |    | |  Dictionary consisting of JSON payload to pass to the HTTP Request | 












#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
response |  success  |   dict  |   Response of the HTTP request  |   {'errorCode': 0, 'errorMessage': ''}  |




#### Examples

```
- name: "REQUEST"
  commvault.ansible.request:
    method: 'GET'
    url: '{0}/cvdrbackup/info'
  register: response

- name: "REQUEST_RESTART_SERVICES"
    commvault.ansible.request:
    method: 'POST'
    url: '{0}/services/action/restart'
    payload:
      "action": 2
      "client": 
        "clientName": "client"
      "services":
        "allServices": true

- name: "REQUEST"
  commvault.ansible.request:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    method: 'GET'
    url: '{0}/cvdrbackup/info'
  register: response


```



















---



## commvault.ansible.deployment.install_software <a name="commvault.ansible.deployment.install_software"></a>
To perform Push Installation from the Commserve


#### Synopsis
 This module performs a Fresh Push Installation to Client Machine from the CommCell
 commvault.ansible.deployment.install_software module can be used in playbooks to perform Push Installs to Clients












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
os_type  |   yes  |  | <ul> <li>windows</li>  <li>unix</li> </ul> |  Client machine operating system category | 
client_computers  |   yes  |  | |  List of Hostnames of the Client Computers to perform a Push installion |  Provide Windows Hostnames (or) Unix Hostnames but never both together | 
windows_package  |   no  |    | <ul> <li>ACTIVE_DIRECTORY</li>  <li>CLOUD_APPS</li>  <li>DOMINO_DATABASE</li>  <li>EXCHANGE</li>  <li>FILE_SYSTEM</li>  <li>MEDIA_AGENT</li>  <li>SHAREPOINT</li>  <li>ORACLE</li>  <li>POSTGRESQL</li>  <li>SQLSERVER</li>  <li>VIRTUAL_SERVER</li>  <li>VSS_PROVIDER</li>  <li>WEB_CONSOLE</li>  <li>TEST_AUTOMATION</li>  <li>PYTHON_SDK</li>  <li>COMMSERVE_LITE</li>  <li>CONTENT_ANALYZER</li> </ul> |  list of windows features to be installed | 
unix_packages  |   no  |    | <ul> <li>CASSANDRA</li>  <li>CLOUD_APPS</li>  <li>DOMINO_DATABASE</li>  <li>FILE_SYSTEM</li>  <li>FILE_SYSTEM_FOR_IBMI</li>  <li>FILE_SYSTEM_FOR_OPEN_VMS</li>  <li>MEDIA_AGENT</li>  <li>ORACLE</li>  <li>POSTGRESQL</li>  <li>SAPHANA</li>  <li>SQLSERVER</li>  <li>VIRTUAL_SERVER</li>  <li>TEST_AUTOMATION</li>  <li>PYTHON_SDK</li>  <li>CONTENT_ANALYZER</li> </ul> |  list of unix features to be installed | 
username  |   no  |    | |  username of the machine to install features on | 
password  |   no  |    | |  Password of the machine to install features on | 
install_path  |   no  |    | |  Install to a specified path on the client | 
client_group_name  |   no  |    | |  List of the client groups for the client | 
storage_policy_name  |   no  |    | |  Storage policy for the default subclient | 
sw_cache_client  |   no  |    | |  Remote Cache Client Name/ Over-riding Software Cache | 
ma_index_cache_loaction  |   no  |    | |  Index Cache location of the Media Agent package | 
wait_for_job_completion  |   no  |  True  | |  Will wait for Download Job to Complete | 














#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
job_id |  success  |   str  |   Push Software Job ID  |   2016  |




#### Examples

```
# Run a Push Installation to the client from Commserver.

- name: "INSTALL_SOFTWARE/PUSH_INSTALL"
  commvault.ansible.deployment.install_software:
    os_type: "windows"
    client_computers:
      - hostname1.example.com
      - x.x.x.x
    windows_packages:
      - FILE_SYSTEM
      - PYTHON_SDK
    username: "domain\username"
    password: "password"
    client_group_name:
      - random_group1
      - random_group2
      - random_group3
    install_path: "D:\Random"
    sw_cache_client: "RemoteCacheClient1"
    wait_for_job_completion: False

- name: "INSTALL_SOFTWARE/PUSH_INSTALL_WINDOWS"
  commvault.ansible.deployment.install_software:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    os_type: "unix"
    client_computers:
      - hostname1.example.com
      - x.x.x.x
    windows_packages:
      - FILE_SYSTEM
      - PYTHON_SDK
    username: "domain\username"
    password: "password"
    client_group_name:
      - random_group1
      - random_group2
      - random_group3
    install_path: "D:\Random"
    sw_cache_client: "RemoteCacheClient1"
    wait_for_job_completion: True

- name: "INSTALL_SOFTWARE/PUSH_INSTALL_UNIX"
  commvault.ansible.deployment.install_software:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    os_type: "unix"
    client_computers:
      - hostname1.example.com
      - x.x.x.x
    unix_packages:
      - MEDIA_AGENT
      - FILE_SYSTEM
    username: "root"
    password: "password"
    client_group_name:
      - random_group1
      - random_group2
      - random_group3
    install_path: "/opt/commvault/ansibledeployment"
    ma_index_cache_location: "/opt/commvault/ma_index_cache"
    sw_cache_client: "RemoteCacheClient1"

notes: 
    Either Windows Packages can be provided or Unix Packages but never both together; 
    Cross platform(Windows & Unix) Push Installation not Supported


```















#### Notes


- windows_package option required only for Windows Client Installations & None for Unix Client Installations

- unix_packages option required only for Unix Client Installations & None for Windows Client Installations








---



## commvault.ansible.deployment.download_software <a name="commvault.ansible.deployment.download_software"></a>
To perform Download Software on Commserve


#### Synopsis
 This module Downloads Media/Latest Payload from the Internet
 commvault.ansible.deployment.download_software module can be used in playbooks to perform Download Software on CS












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
download_option  |   no  |  LATEST_SERVICEPACK  | <ul> <li>LATEST_SERVICEPACK</li>  <li>LATEST_HOTFIXES</li>  <li>SERVICEPACK_AND_HOTFIXES</li> </ul> |  Download option to download software | 
os_list  |   no  |    | <ul> <li>WINDOWS_32</li>  <li>WINDOWS_64</li>  <li>UNIX_AIX</li>  <li>UNIX_AIX32</li>  <li>UNIX_MAC</li>  <li>UNIX_FREEBSD86</li>  <li>UNIX_FREEBSD64</li>  <li>UNIX_HP</li>  <li>UNIX_LINUX86</li>  <li>UNIX_LINUX64</li>  <li>UNIX_S390</li>  <li>UNIX_S390_31</li>  <li>UNIX_PPC64</li>  <li>UNIX_SOLARIS86</li>  <li>UNIX_SOLARIS64</li>  <li>UNIX_SOLARIS_SPARC</li>  <li>UNIX_SOLARIS_SPARC86</li>  <li>UNIX_LINUX64LE</li> </ul> |  list of windows/unix packages to be downloaded | 
service_pack  |   no  |    | |  service pack to be downloaded | 
cu_number  |   no  |  0  | |  maintenance release number | 
sync_cache  |   no  |  True  | |  Download/Sync the Remote Cache | 
wait_for_job_completion  |   no  |  True  | |  Will wait for Download Job to Complete | 














#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
job_id |  success  |   str  |   Download Software Job ID  |   2016  |




#### Examples

```
# Run a Download Job on the Commserver.

- name: "DOWNLOAD_SOFTWARE"
  commvault.ansible.deployment.download_software:
    download_option: "LATEST_SERVICEPACK"
    os_list:
      - WINDOWS_64
      - UNIX_LINUX64
    sync_cache: False
    wait_for_job_completion: False

- name: "DOWNLOAD_SOFTWARE"
  commvault.ansible.deployment.download_software:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    download_option: "LATEST_SERVICEPACK" (or)  "LATEST_HOTFIXES"
    os_list:
      - WINDOWS_64
      - UNIX_LINUX64
    sync_cache: False

- name: "DOWNLOAD_SOFTWARE"
  commvault.ansible.deployment.download_software:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    download_option: "SERVICEPACK_AND_HOTFIXES"
    os_list:
      - WINDOWS_64
      - UNIX_LINUX64
    service_pack: 23
    cu_number: 2
    sync_cache: False
    wait_for_job_completion: False
      

```















#### Notes


- {'Service_pack option required only with the Download Option': 'SERVICEPACK_AND_HOTFIXES'}








---



## commvault.ansible.deployment.push_updates <a name="commvault.ansible.deployment.push_updates"></a>
To Push Updates to the Clients from Commserver


#### Synopsis
 This module pushes latest Updates to client from CommCell
 commvault.ansible.deployment.push_updates module can be used in playbooks to perform Push Updates to Clients












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
client_names  |   no  |    | |  List of Client Names(Name on Commcell) to install service pack on | 
client_group_names  |   no  |    | |  list of Client groups to install service pack on | 
update_all_client_computers  |   no  |  False  | |  boolean to specify whether to install on all clients | 
update_all_client_computer_groups  |   no  |  False  | |  boolean to specify whether to install on all clients groups | 
reboot_client  |   no  |  False  | |  boolean to specify whether to reboot the client or not while installing updates | 
run_db_maintenance  |   no  |  True  | |  boolean to specify whether to run rb maintenance or not | 
install_maintenance_release_only  |   no  |  False  | |  boolean to specify whether to install only Maintenance Release or Not | 
wait_for_job_completion  |   no  |  True  | |  Will wait for Download Job to Complete | 












#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
job_id |  success  |   str  |   Push Updates Job ID  |   2016  |




#### Examples

```
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


```



















---



## commvault.ansible.file_servers.manage_content <a name="commvault.ansible.file_servers.manage_content"></a>
To update the properties of a file server at subclient level.


#### Synopsis
 commvault.ansible.file_servers.manage_content can be used to update the content, filters and exceptions of a File System subclient.
 keys for 'update' are 'content', 'filter_content', 'exception_content' & will ALWAYS OVERWRITE existing values.












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
client  |   yes  |  | |  The name of the client. | 
backupset  |   no  |  | |  The name of the backupset. | 
subclient  |   no  |  | |  The name of the subclient. | 
update  |   yes  |  | <ul> <li>content</li>  <li>filter_content</li>  <li>exception_content</li> </ul> |  A dictionary of updates to make where update is a dictionary with key is property name & value is property value. |  choices specifies the supported key values. | 
















#### Examples

```
- name: Update a File System subclient's content and filter, session file would be used.
  commvault.ansible.file_servers.manage_content:
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    update:
        content:
            - C:\ANSIBLE_PATH1
            - C:\ANSIBLE_PATH2
        filter_content:
            - C:\ANSIBLE_PATH1\FILTER1
            - C:\ANSIBLE_PATH1\FILTER2      

- name: Update a File System subclient's content and filter.
  commvault.ansible.file_servers.manage_content:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    update:
        content:
            - C:\ANSIBLE_PATH1
            - C:\ANSIBLE_PATH2
        filter_content:
            - C:\ANSIBLE_PATH1\FILTER1
            - C:\ANSIBLE_PATH1\FILTER2                  

```





















---



## commvault.ansible.file_servers.backup <a name="commvault.ansible.file_servers.backup"></a>
To perform backup of a file server subclient.


#### Synopsis
 commvault.ansible.file_servers.backup can be used to perform file server backup operation.












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
client  |   yes  |  | |  The name of the Client. | 
backupset  |   no  |  default backupset  | |  The name of the backupset. | 
subclient  |   no  |  subclient named default.  | |  The name of the subclient. | 
backup_level  |  no  |  Incremental  |  <ul> <li>Full</li> <li>Incremental</li> <li>Differential</li> <li>Synthetic_full</li> </ul>  |  Backup Level.  |
agent_type  |  no  |  File System  | <ul> <li>File System</li> <li>Linux File System</li> </ul>  |  Agent Type.  |














#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
job_id |  On success  |   str  |   Backup job ID  |   2016  |




#### Examples

```
- name: Run an incremental(default) File System Backup for default subclient of default backupset, session file would be used.
  commvault.ansible.file_servers.backup:
    client: "client_name"

- name: Run an incremental(default) File System Backup for subclient 'user_subclient' of backupset 'user_backupset', session file would be used.
  commvault.ansible.file_servers.backup:
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
        
- name: Run an incremental(default) File System Backup for default subclient of default backupset.
  commvault.ansible.file_servers.backup:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    client: "client_name"

- name: Run an incremental(default) File System Backup for subclient 'user_subclient' of backupset 'user_backupset'.
  commvault.ansible.file_servers.backup:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"

- name: Run an incremental(default) File System Backup for subclient 'user_subclient' of backupset 'user_backupset'i with agent_type of Linux File System.
  commvault.ansible.file_servers.backup:
    webserver_hostname: "web_server_hostname"
    commcell_username: "user"
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    agent_type: "Linux File System"

- name: Run a full File System Backup for subclient 'user_subclient' of backupset 'user_backupset' specifying 'backup_level' as Full.
  commvault.ansible.file_servers.backup:
    webserver_hostname: "web_server_hostname"
    commcell_username: "user"
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    backup_level: "Full"


```





















---



## commvault.ansible.file_servers.manage_plan <a name="commvault.ansible.file_servers.manage_plan"></a>
To change the plan associated to the client, backupset or subclient.


#### Synopsis
 commvault.ansible.file_servers.manage_plan can be used to change the server plan associated at the client, backupset or subclient level.












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
client  |   yes  |  | |  The name of the client. | 
plan  |   yes  |  | |  The name of the server plan which needs to be associated to the entity. | 
backupset  |   no  |  | |  The name of the backupset. | 
subclient  |   no  |  | |  The name of the subclient. | 














#### Examples

```
- name: Associate a client to plan 'server plan', session file will be used.
  commvault.ansible.file_servers.manage_plan:
    client: "client_name"
    plan: "server plan"

- name: Associate a user created subclient to plan 'server plan'.
  commvault.ansible.file_servers.manage_plan:
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    plan: "server plan"
    
- name: Associate a user created subclient to plan 'server plan'.
  commvault.ansible.file_servers.manage_plan:
    webserver_hostname: "web_server_hostname"
    commcell_username: "user"
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    plan: "server plan"
author:
- Commvault Systems Inc 

```



















---



## commvault.ansible.file_servers.restore <a name="commvault.ansible.file_servers.restore"></a>
To perform restore of a file server subclient.


#### Synopsis
 commvault.ansible.file_servers.restore can be used to perform a file server restore operation.












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
client  |   yes  |  | |  The name of the client. | 
backupset  |   no  |  default backupset  | |  The name of the backupset. | 
subclient  |   no  |  subclient named 'default'.  | |  The name of the subclient. | 
agent_type  |  no  |  File System  | <ul> <li>File System</li> <li>Linux File System</li> </ul>  |  Agent Type.  |
content  |   yes  |  | |  The path of the content that needs to be restored. | 
in_place  |   no  |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  Whether the content needs to be restored in place i.e. restored back to the source location. | 
destination_path  |   no  |  | |  Destination path in case the content needs to be restored to another location. | 
unconditional_overwrite  |   no  |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  Specifies whether data needs to be overwritten at the destination if the file already exists. | 














#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
job_id |  On success  |   str  |   Restore job ID  |   2017  |




#### Examples

```
- name: Run a File System Restore for default subclient of default backupset, session file will be used.
  commvault.ansible.file_servers.restore:
    client: "client_name"
    content: "C:\path\of\content"

- name: Run a File System Restore for subclient 'user_subclient' of backupset 'user_backupset', session file will be used.
  commvault.ansible.file_servers.restore:
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    content: "C:\path\of\content"

- name: Run a File System Restore for subclient 'user_subclient' of backupset 'user_backupset' and agent_type of Linux File System, session file will be used.
  commvault.ansible.file_servers.restore:
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    agent_type: "Linux File System"
    content: "C:\path\of\content"
    
- name: Run an In-Place File System Restore for subclient 'user_subclient' of backupset 'user_backupset'.
  commvault.ansible.file_servers.restore:
    webserver_hostname: "web_server_hostname"
    commcell_username: "user"
    commcell_password: "password"
    client: "client_name"
    backupset: "user_backupset"
    subclient: "user_subclient"
    content: "C:\path\of\content"
    in_place: "yes"



```





















---



## commvault.ansible.job.kill <a name="commvault.ansible.job.kill"></a>
kills the Job


#### Synopsis
 This module kills the job
 commvault.ansible.job.kill module can be used in playbooks to kill the job












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
job_id  |   yes  |  | |  ID of the job | 
wait_for_job_to_kill  |   no  |  False  | |  wait till job status is changed to Killed | 














#### Examples

```
# kills a particular Job

- name: "Kill Job"
  commvault.ansible.job.kill:
    job_id: 3

- name: "kill Job"
  commvault.ansible.job.kill:
    job_id: 7
    wait_for_job_to_kill: False

- name: "kill Job and Wait for kill Task to be completed"
  commvault.ansible.job.kill:
    job_id: 18
    wait_for_job_to_kill: True

- name: "kill Job"
  commvault.ansible.job.kill:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    job_id: 23


```



















---



## commvault.ansible.job.resume <a name="commvault.ansible.job.resume"></a>
Resumes the Job


#### Synopsis
 This module resumes the job
 commvault.ansible.job.resume module can be used in playbooks to resume the job












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
job_id  |   yes  |  | |  ID of the job | 
wait_for_job_to_resume  |   no  |  False  | |  wait till job status is changed to Running | 














#### Examples

```
# Resumes a particular Job

- name: "Resume Job"
  commvault.ansible.job.resume:
    job_id: 3

- name: "Resume Job"
  commvault.ansible.job.resume:
    job_id: 7
    wait_for_job_to_resume: False

- name: "Resume Job and Wait for Resume Task to be completed"
  commvault.ansible.job.resume:
    job_id: 18
    wait_for_job_to_resume: True

- name: "Resume Job"
  commvault.ansible.job.resume:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    job_id: 23


```



















---



## commvault.ansible.job.status <a name="commvault.ansible.job.status"></a>
Checks the status of the Job


#### Synopsis
 This module Checks the Job Status
 commvault.ansible.job.status module can be used in playbooks to check the job status












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
job_id  |   yes  |  | |  ID of the job | 
wait_for_job_completion  |   no  |  False  | |  wait till job status is changed to Completed/Failed | 












#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
job_id |  |   str  |   Status of the Job  |   Running/Completed  |




#### Examples

```
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


```



















---



## commvault.ansible.job.suspend <a name="commvault.ansible.job.suspend"></a>
Suspends the Job


#### Synopsis
 This module suspends the job
 commvault.ansible.job.suspend module can be used in playbooks to suspend the job












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
job_id  |   yes  |  | |  ID of the job | 
wait_for_job_to_suspend  |   no  |  False  | |  wait until job status is changed to Suspended | 














#### Examples

```
# Suspends a particular Job

- name: "Suspend Job"
  commvault.ansible.job.suspend:
    job_id: 3

- name: "Suspend Job"
  commvault.ansible.job.suspend:
    job_id: 7
    wait_for_job_to_suspend: False

- name: "Suspend Job and Wait for Suspend Task to be completed"
  commvault.ansible.job.suspend:
    job_id: 18
    wait_for_job_to_suspend: True

- name: "Suspend Job"
  commvault.ansible.job.suspend:
    webserver_hostname: "demo-CS-Name"
    commcell_username: "user"
    commcell_password: "CS-Password"
    job_id: 23


```



















---



## commvault.ansible.plans.add <a name="commvault.ansible.plans.add"></a>
Creates a plan


#### Synopsis
 This module creates a Plan in the CommCell












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
name  |   yes  |  | |  The name of the plan. | 
storage_pool_name  |   yes  |  | |  The name of the storage to use for the plan. | 
type  |   no  |  Server  | <ul> <li>Server</li>  <li>Laptop</li>  <li>ExchangeUser</li> </ul> |  The type of plan to create. | 
rpo_minutes  |   no  |  1440  | |  The Recovery Point Objective time in minutes for the plan. Default is 1440 minutes (24 hours) | 














#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
name |  Success  |   str  |   The name of the plan created  |   Plan 1  |id |  Success  |   str  |   The ID of the plan created  |   2  |




#### Examples

```
- name: Creating a plan
  commvault.ansible.plans.add:
    name: "Plan 1"
    storage_pool_name: "storage2"

- name: Creating a plan with 7 days RPO
  commvault.ansible.plans.add:
    name: "Plan 1"
    storage_pool_name: "storage2"
    rpo_minutes: 10080

- name: Creating a "Server" plan with 2 days RPO
  commvault.ansible.plans.add:
    name: "Plan 1"
    type: "Server"
    storage_pool_name: "storage2"
    type: "Server"
    rpo_minutes: 2880

- name: Creating a "Server" plan with 2 days RPO
  commvault.ansible.plans.add:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    name: "Plan 1"
    type: "Server"
    storage_pool_name: "storage2"
    rpo_minutes: 2880

```





















---



## commvault.ansible.plans.delete <a name="commvault.ansible.plans.delete"></a>
Deletes a plan


#### Synopsis
 This module deletes a Plan in the CommCell












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
name  |   yes  |  | |  The name of the plan to delete. | 
















#### Examples

```
- name: Deleting plan
  commvault.ansible.plans.delete:
    name: "Plan 1"

- name: Deleting plan
  commvault.ansible.plans.delete:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    name: "Plan 1"

```





















---



## commvault.ansible.workflow.execute <a name="commvault.ansible.workflow.execute"></a>
Executes the workflow with the workflow name and inputs


#### Synopsis
 This module executes the given Workflow along with it's inputs
 commvault.ansible.workflow.execute module can be used in playbooks to execute the Workflows on client from Commcell












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
workflow_name  |   yes  |  | |  Name of the Workflow | 
workflow_inputs  |   yes  |  | |  Dictionary consisting of inputs to execute the workflow | 
hidden_workflow  |   no  |  False  | |  Is the workflow hidden ? | 












#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
job_id |  success  |   str  |   Relevant workflow job ID (-1 if N/A)  |   2016  |




#### Examples

```
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


```



















---



## commvault.ansible.workflow.deploy <a name="commvault.ansible.workflow.deploy"></a>
Deploys a workflow on the Commcell.


#### Synopsis
 Deploys a workflow on the Commcell.
 commvault.ansible.workflow.deploy module can be used in playbooks to Deploys a workflow on the Commcell.












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
workflow_name  |   yes  |  | |  Name of the Workflow | 
workflow_engine  |   yes  |  | |  name of the client to deploy the workflow on | 
workflow_xml_path  |   yes  |  | |  path of the workflow xml file / XMl contents | 














#### Examples

```
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


```



















---



## commvault.ansible.workflow.export <a name="commvault.ansible.workflow.export"></a>
Exports the workflow to the directory location specified by the user.


#### Synopsis
 Exports the workflow XML to the directory location specified by the user.
 commvault.ansible.workflow.export module can be used in playbooks to export the workflow to the directory location specified by the user.












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
workflow_name  |   yes  |  | |  Name of the Workflow | 
export_location  |   yes  |  | |  Directory where the workflow would be exported | 














#### Examples

```
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


```



















---



## commvault.ansible.workflow.import <a name="commvault.ansible.workflow.import"></a>
Imports a workflow to the Commcell.


#### Synopsis
 Imports a workflow to the Commcell.
 commvault.ansible.workflow.import module can be used in playbooks to import a workflow on the Commcell.












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Username | 
commcell_password  |   no  |  | |  Password | 
workflow_name  |   yes  |  | |  Name of the Workflow | 
workflow_xml_path  |   yes  |  | |  path of the workflow xml file / XMl contents | 














#### Examples

```
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


```



















---



## commvault.ansible.storage.disk.detail <a name="commvault.ansible.storage.disk.detail"></a>
Gets details of a disk storage


#### Synopsis
 This module gets details of a given disk storage












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
name  |   yes  |  | |  The name of the disk storage pool. | 














#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
detail |  Success  |   dict  |   Details of the disk storage  |   |




#### Examples

```
- name: "Getting details of disk storage"
  commvault.ansible.storage.disk.detail:
    name: "storage2"

- name: "Getting details of disk storage"
  commvault.ansible.storage.disk.detail:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    name: "storage2"

```





















---



## commvault.ansible.storage.disk.add <a name="commvault.ansible.storage.disk.add"></a>
Creates a disk storage


#### Synopsis
 This module creates a disk storage in the CommCell












#### Options
| Parameter     | required    | default  | choices    | comments |
| ------------- |-------------| ---------|----------- |--------- |
webserver_hostname  |   no  |  | |  Hostname of the Web Server. | 
commcell_username  |   no  |  | |  Commcell username | 
commcell_password  |   no  |  | |  Commcell password | 
name  |   yes  |  | |  The name of the disk storage pool. | 
media_agent  |   yes  |  | |  The name of the media agent to create the disk storage for. | 
mount_path  |   yes  |  | |  The path of the disk storage. | 
deduplication_db_path  |   yes  |  | |  The path of the deduplication DB storage | 














#### Returns
| Name          | Returned    | Type     | Description | Sample |
| ------------- |-------------| ---------|-----------  |--------|
name |  Success  |   str  |   The name of the disk storage created  |   storage2  |id |  Success  |   str  |   The ID of the disk storage created  |   12  |




#### Examples

```
- name: Creating disk storage
  commvault.ansible.storage.disk.add:
    name: "storage2"
    media_agent: "cv_mediaagent_1"
    mount_path: "D:\storage2"
    deduplication_db_path: "D:\ddb_path2"

- name: Creating disk storage
  commvault.ansible.storage.disk.add:
    webserver_hostname: "web_server_hostname" 
    commcell_username: "user"  
    commcell_password: "password"
    name: "storage2"
    media_agent: "cv_mediaagent_1"
    mount_path: "D:\storage2"
    deduplication_db_path: "D:\ddb_path2"

```





















---



---

Questions/Comments/Suggestions
------------------------------
If you have any questions or comments, please contact us [here](https://ma.commvault.com/).
Also Check out our community for [Automation](https://community.commvault.com/developer-tools-integration-and-automation-workflow-rest-powershell-etc-50) incase of queries.
