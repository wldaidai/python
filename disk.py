#!/usr/bin/python
import re
import commands
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import sys

mail_host = 'smtp.163.com'
mail_user = '15068715180'
mail_pass = 'mima10086'
mail_postfix = '163.com'

def send_mail(to_list,subject,content):
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

disk_use=int(commands.getoutput('df -h|grep -w "/"').split()[-2].split('%')[0])
ip_list=commands.getoutput('ifconfig|grep "inet addr"').split("\n")
r=".*inet addr:(.*) Bcast"
for ip in ip_list:
    if re.match(r,ip):
       ip_tmp=re.match(r,ip)
       ipl=ip_tmp.group(1)
       if ipl.split(".")[0] == "192" or ipl.split(".")[0] == "127" or ipl.split(".")[0] == "10":
           pass
       else:
           ipt=ipl 
            
if disk_use > 80:
    message=ipt+"disk is problem for use then 80%"
    send_mail("15068715180@139.com","disk problem",message)
else:
    pass


