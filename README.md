# Zabbix Cohesity Back up Solution Integration
## Overview

Template Zabbix + API Request using Cohesity Management SDK to Collect the Protection job Status .
https://github.com/cohesity/management-sdk-python

https://share.zabbix.com/cat-app/backup/cohesity-backup-solution

## Installation

### Zabbix Server

 1. Install the Cohesity Management SDK.
 

pip install cohesity-management-sdk

 2. Verify API Variables :
 ```
username = 'Username'
password = 'Password'
domain = 'Domain' #optional
cluster_vip = 'prod-cluster.eng.cohesity.com' #Cluster IP
```

3. Run Tests
	python /usr/local/lib/python2.7/dist-packages/samples/protection_runs_status/protection_run_status.py
		
    ('06-01-2021 03:00:02', u'xxxxxxxx', xxxxx, u'kSuccess')

    ('06-01-2021 02:00:01', u'xxxxxxxx', xxxxx, u'kSuccess')

    ('06-01-2021 01:00:01', u'xxxxxxxx', xxxxx, u'kSuccess')

    ('05-31-2021 13:00:01', u'xxxxxxxx', xxxxx, u'kSuccess')


4. so far so good .
5. copy file version in the project to your python environments. and run the script with env variables.
6. Chmode the required permissions.

python /usr/local/lib/python2.7/dist-packages/samples/protection_runs_status/protection_run_status_v2.py #JOBNAME
Scripts will return Following Values based on the result of job.

    status == 'kSuccess'   : "2"
    status == 'kRunning'   : "5"
    status == 'kWarning'   : "1"
    status == 'kCancelled' : "4"
    status == 'kError' 	: "0" 
7. Update zabbix agent conf  on the zabbix server 

    EnableRemoteCommands=1
    UserParameter=uPJD.discovery,python /usr/local/lib/python2.7/dist-packages/samples/protection_runs_status/protection_run_status_v2.py

    UserParameter=uPJD.value[*],python /usr/local/lib/python2.7/dist-packages/samples/protection_runs_status/protection_run_status_v2.py $1

8. add the template Cohesity to the Zabbix server host.
9. Zabbix Agent need to be running on the host in which Cohesity SDK is installed.
10. passing the Space in the name of job will result in error.
11. Thanks.
