#!/usr/bin/python
import sys
s=[1,2,3,4]
for i in range(20,100):
    if i%s[0]==0 and i%s[1]==0 and i%s[2]==0 and i%s[3]==0:
        print i
        sys.exit()
        
            
       
