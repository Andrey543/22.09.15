import robot
import time
r = robot.rmap()
r.lm('task1')

def task():
    i1=r.getCoordR()
    i2=r.getCoordC()
    #r.pt('yellow')
    print(i1,i2)
    i=1
    while i<i2:
        r.lt(1)
        i+=1
    i=1
    while i<i1:
        r.up(1)
        i+=1
    i=0
    j=0
    k=0
    while i<19:
        while j<18:
            if r.label():
                k=1
                break
            r.rt(1)
            j+=1
        if k:
            break
        r.lt(18)
        r.dn(1)
        i+=1
        j=0  
    k=0    
    time.sleep(1)
    while r.label():
        if r.fr()-1:
            k+=1
            break
        k+=1
        r.rt(1)
    l=0    
    r.lt(1)
    while r.label():
        if r.fr()-1:
            l+=1
            break
        l+=1
        r.dn(1)
    print(l*k)            
r.start(task)
