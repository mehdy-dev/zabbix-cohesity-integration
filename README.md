# Zabbix Cohesity Back up Solution Integration
## Overview

Template Zabbix + API Request using Cohesity Management SDK to Collect the Protection job Status .


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
('05-31-2021 23:30:01', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 15:00:01', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 20:00:02', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 06:00:01', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 06:00:01', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 22:00:00', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 18:00:00', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 18:30:01', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 20:00:02', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 22:00:00', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 22:00:00', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 10:00:00', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 12:30:01', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 22:00:00', u'xxxxxxxx', xxxxx, u'kSuccess')
('05-31-2021 22:00:00', u'xxxxxxxx', xxxxx, u'kSuccess') 

4. so far so good .
5. copy the file in the project to your python environments.
6. 
