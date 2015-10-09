#!/usr/bin/python
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
