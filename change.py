#!/usr/bin/python
# -*- coding: utf-8 -*-

file="/usr/local/src/python-master/fwq.host"
li=[]

with open(file,'r') as f:
    for line in f.readlines():
        date=line.split()[2].split("/")[0]
        date_now=str(int(line.split()[2].split("/")[0])+1)
        new_line=line.replace(date,date_now)
        li.append(new_line)
with open(file,'w+') as w:
    w.writelines(li)
 
