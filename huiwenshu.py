#!/usr/bin/python
s=[]
for i in range(10,100):
    for n in range(i,100):
        a=i*n
        b=str(a)
        for f in range(len(b)/2):
            if b[f]!=b[len(b)-f-1]:
                flag = False
            else:
                flag = True
            if flag:
                s.append(a)
print sorted(s)[-1]
               
       
        
