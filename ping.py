#!/usr/bin/python
import re
import os
import sendmail


def Ping(ip):
    lip=re.compile(".*loss")
    os.system('ping -w 10 %s >/data/scripts/ls.txt' %ip)
    with open('ls.txt','r') as f:
        for i in f.readlines():
            if lip.findall(i):
                if int(i.split(' ')[5].split('%')[0]) > 5:
                    message='%s network is bad' %ip
                    sendmail.send_mail("15068715180@139.com","network error",message)
                else:
                    sendmail.send_mail("15068715180@139.com","network ok","ok") 
with open('php_host','r') as f:
    for ip in f.readlines():
        Ping(ip)

