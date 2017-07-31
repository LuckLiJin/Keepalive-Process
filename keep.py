#!/usr/bin/python
#coding:utf8

import os
import psutil
from time import sleep, ctime, localtime
from tabulate import tabulate

def start_process():
    cmdline = "/usr/bin/python /root/myPython/test/redis-server.py test.conf 1>/dev/null  2>1  &"
    os.system(cmdline)
    print ctime(), "Process restart"

def found_process():
    pro_list = psutil.get_process_list()
    headers = ['pid', 'ppid', 'name', 'cmdline']
    table = []
    res = False
    for pro in pro_list:
        if 'redis' in ' '.join(pro.cmdline):
            table.append((pro.pid, pro.ppid, pro.name, ' '.join(pro.cmdline)))
            res = True
            #pro.kill()
    print tabulate(table, headers = headers)
    return res


if __name__ == "__main__":

    while True:
        if not found_process():
            start_process()
        sleep(10.0)
