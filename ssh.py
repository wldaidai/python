#!/usr/bin/python 
#by larry 
#2011/01/30 
import paramiko
import datetime
import threading

def ssh(name):
    file=open(name,'r')
    threads=[]
    for line in file.readlines():
        the(line)
def the(name):
    port=9404 
    username='root' 
    hostname=str(name.split(' ')[0]) 
    password=str(name.split(' ')[3]).strip()
    print "##########################",hostname,"########################" 
    s=paramiko.SSHClient() 
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    s.connect(hostname,port,username,password) 
    stdin,stdout,sterr=s.exec_command('df -Th') 
    print stdout.read()
    s.close 

if __name__=='__main__':
    starttime = datetime.datetime.now()
    ssh('ip.list')
    endtime = datetime.datetime.now()
    print (endtime-starttime).seconds



