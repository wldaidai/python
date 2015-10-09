#!/usr/bin/python
import MySQLdb

def select(table,value,item,res):
    try:
        conn=MySQLdb.connect(host='localhost',user='root',db='shop',port=3306)
        cur=conn.cursor()
        sql="select "+value+" from "+table+" where "+item+"="+"%s"
        cur.execute(sql,res)
        rows = cur.fetchmany(1)
        return rows
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def update(username,money):
    try:
        conn=MySQLdb.connect(host='localhost',user='root',db='shop',port=3306)
        cur=conn.cursor()
        sql="update user set count=%s where username='%s'" %(money,username)
        cur.execute(sql)
        rows = cur.fetchmany(1)
        return rows
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def buy():
    name=raw_input("please input your name ")
    count=str(select ('user','count','username',name)[0]).split('L')[0].split('(')[1]
    if count:
        item=raw_input("please input you want to buy things ")
        num=int(raw_input("please input The number of things you want to buy "))
        price=int(str(select ('item','price','item',item)[0]).split('L')[0].split('(')[1])
        if count > price*num:
            s_money=int(count)-price*num
            update(name,s_money)
            print "Your account balance is",s_money
        else:
            print "Your account balance is not enough"

buy()
            
             
