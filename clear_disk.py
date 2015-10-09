#!/usr/bin/python
import commands
import os
import time
disk_use=int(commands.getoutput('df -h|grep -w "/"').split()[-2].split('%')[0])
app_list=os.listdir('/usr/local')

if "tengine" in app_list:
    log_dir="/usr/local/tengine/logs/"
else:
    log_dir="/usr/local/nginx/logs/"

if disk_use > 80:
    log_list=os.listdir(log_dir)
    time_now=time.strftime('%m-%d',time.localtime())
    for log in log_list:
        log_name=os.path.join(log_dir,log)
        time_log=time.strftime('%m-%d',time.localtime(os.path.getmtime(log_name)))
        if time_log.split('-')[0] == time_now.split('-')[0] and int(time_now.split('-')[1])-int(time_log.split('-')[1])>3:
            os.remove(log_name)
         
    
    
