#opyright 2019 Cohesity Inc.
#
# Python example to get a status of a protection run
#
# Usage: python protection_run_status.py

import datetime
import json
import sys
from cohesity_management_sdk.cohesity_client import CohesityClient


CLUSTER_VIP = 'xxxxxxxxx'
CLUSTER_USERNAME = 'xxxxxxxx'
CLUSTER_PASSWORD = 'xxxxxxxxxxxxxx'
DOMAIN = 'xxxxxxxxxxxx'

class jobs:
    def __init__(self, name, result):
        self.name = name
        self.result = result


class ProtectionRunsList(object):

    def display_protection_runs(self, cohesity_client,argv_1):
        """
        Method to display the list of protection runs
        :param cohesity_client(object): Cohesity client object.
        :return:
        """
        protection_runs = cohesity_client.protection_runs
        run_list = protection_runs.get_protection_runs()
        list_obj = []
        res_str= ''
 
		if argv_1 is None:
                for run in run_list:
                        # print(self.epoch_to_date(run.backup_run.stats.start_time_usecs), run.job_name, run.backup_run.job_run_id, run.backup_run.status)
                        list_obj.append(jobs(run.job_name,run.backup_run.status))
                        # print(run.job_name)
                res_str += '{'
                        #print('{')
                        #print '"data"',':','['
                res_str += '"data"'+':'+'['
                count = len(list_obj)
                for jsonobj in list_obj:
                        count -=1
                        ResJson = json.dumps(jsonobj.name)
                        #jsonPrint = '"'+jsonobj.name+'"'
                        #print '{','"#PJ"',':',ResJson,'}',','
                        if count == 0 :
                                res_str += '{'+'"{#PJ}"'+':'+ResJson+'}'
                        else :
                                res_str += '{'+'"{#PJ}"'+':'+ResJson+'}'+','
                #print(']')
                res_str += ']'
                res_str += '}'
                print(res_str)
                #print('}')
                #print(json.dumps(list_obj[0].name))
        else :
                for run in run_list:
                # print(self.epoch_to_date(run.backup_run.stats.start_time_usecs), run.job_name, run.backup_run.job_run_id, run.backup_run.status)
                        list_obj.append(jobs(run.job_name,run.backup_run.status))
                        # print(run.job_name)
                res_str += '{'
                        #print('{')
                        #print '"data"',':','['
                res_str += '"data"'+':'+'['
                res_null = res_str
                count = len(list_obj)
                returnval = "NULL"
                status = json.dumps(returnval)
                ResJson = json.dumps(argv_1)
                res_null += '{'+'"{#PJ}"'+':'+ResJson+'}'+','+'{'+'"{#STATUS}"'+':'+status+'}'
                ret_val = "7"
 
				for jsonobj in list_obj:
                        if jsonobj.name == argv_1 :
                                ResJson = json.dumps(jsonobj.name)
                                status = jsonobj.result
                                if status == 'kSuccess' :
                                        ret_val = "2"
                                elif status == 'kRunning':
                                        ret_val = "5"
                                elif status == 'kWarning' :
                                        ret_val = "1"
                                elif status == 'kCancelled' :
                                        res_val = "4"
                                elif status == 'kError' :
                                        res_val = "0"
                                res_str += '{'+'"{#PJ}"'+':'+ResJson+'}'+','+'{'+'"{#STATUS}"'+':'+status+'}'
                                res_null = res_str
                        else :
                                returnval = "NULL"
                                #status = json.dumps(returnval)
                                #ResJson = json.dumps(argv_1)
                                #res_str += '{'+'"{#PJ}"'+':'+ResJson+'}'+','+'{'+'"{#STATUS}"'+':'+status+'}'
                res_null += ']'
                res_null += '}'
                #print(res_null)
                print(ret_val)
    @staticmethod
    def epoch_to_date(epoch):
        """
        Method to convert epoch time in usec to date format
        :param epoch(int): Epoch time of the job run.
        :return: date(str): Date format of the job runj.
        """
        date = datetime.datetime.fromtimestamp(epoch/10**6).\
            strftime('%m-%d-%Y %H:%M:%S')
        return date

def main():

    param_1 = sys.argv[1] if len(sys.argv) > 1 else None
    cohesity_client = CohesityClient(cluster_vip=CLUSTER_VIP,
                                     username=CLUSTER_USERNAME,
                                     password=CLUSTER_PASSWORD,
                                     domain=DOMAIN)
    protection_runs = ProtectionRunsList()
    protection_runs.display_protection_runs(cohesity_client,param_1)

if __name__ == '__main__':
    main()
