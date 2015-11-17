import robot
r = robot.rmap()
r.lm('task1')

def task():
    i1=r.getCoordR()
    i2=r.getCoordC()
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
    while i<14:
        while j<9:
            if r.wd():
                r.rt(1)
                if r.wd():
                    k=1
                else: 
                    r.dn(1)
                    r.lt(1)
            else:
                r.dn(1)        
            if k:
                break
            j+=1 
        if k:
            break 
            print(j)
        i+=1
        r.lt(i-1)
        r.up(9)
        r.rt(i)
        j=0    
    r.lt(2)
    r.dn(1)
    r.rt(1)
    while r.wu():
        r.pt('yellow')
        r.rt(1)               
r.start(task)


