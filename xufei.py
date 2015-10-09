#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import sendmail


file="/usr/local/src/python-master/fwq.host"
today=time.strftime('%m-%d',time.localtime())
now=int(today.split("-")[0])*30+int(today.split("-")[1])



def xufei():
    with open(file,'r') as f:
        for line in f.readlines():
            if not line.strip():continue
            ip=line.split()[0]
            money=line.split()[1]
            month=int(line.split()[2].split("/")[0])
            day=int(line.split()[2].split("/")[1])
            date=month*30+day
            if date - now < 5:
                message="%s,需要续费,续费金额为%s" %(ip,money)
                sendmail.send_mail("15068715180@139.com","服务器续费",message)
      
                 
if __name__ == "__main__":            
    xufei()
        
