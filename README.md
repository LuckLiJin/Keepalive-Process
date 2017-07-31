# Keepalive-Process
应用于linux系统，每隔10秒检测一次进程是否存在，若不存在则启动，否则等待


## 环境搭建

sudo pip install tabulate

psutil 为5.2.2 版本

sudo pip install psutil

## 使用说明

打开keep.py文件， 修改 execute 和 conf 两个全局变量

execute 是运行程序名称
conf   是配置文件名称


