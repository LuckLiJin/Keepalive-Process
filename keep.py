#!/usr/bin/python
#coding:utf8

import os
import psutil
from time import sleep, ctime, localtime
from tabulate import tabulate

#修改以下两处参数
execute = '/usr/bin/python'
conf = "/root/myPython/test/redis-server.py"

def start_process():
    global execute, conf
    cmdline = "%s %s 1>/dev/null  2>&1  &" % (execute, conf)
    os.system(cmdline)
    print ctime(), "Process restart"

def found_process():
    global conf
    headers = ['pid', 'ppid', 'name', 'cmdline']
    table = []
    res = False
    for pid in psutil.pids():
        pro = psutil.Process(pid)
        if conf in ' '.join(pro.cmdline()):
            table.append((pro.pid, pro.ppid(), pro.name(), ' '.join(pro.cmdline())))
            res = True
            print tabulate(table, headers = headers)
    return res


if __name__ == "__main__":

    while True:
        if not found_process():
            start_process()
        sleep(10.0)
