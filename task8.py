import robot
r = robot.rmap()
r.lm('task1')

def task():
    i1=r.getCoordR()
    i2=16-r.getCoordC()
    print(i1,i2)
    i=1
    while i<i1:
        r.up(1)
        i+=1
    i=1
    while i<i2:
        r.rt(1)
        i+=1
    i=0
    j=0
    k=0
    while i<9:
        while j<14:
            if r.fl():
                r.lt(1)
            else:
                k=1
                break
            j+=1
        if k:
            break
        i+=1
        j=0  
        r.rt(14) 
        r.dn(1) 
    i=0
    while r.fl()-1:
        r.dn(1)
        i+=1
    r.lt(1)
    j=0
    while j<i:
        r.up(1)
        r.pt('yellow')
        j+=1
    while r.fl():
        r.lt(1)
        r.pt('yellow')
    j=0
    while j<=i:
        r.dn(1)
        r.pt('yellow')
        j+=1
    while r.fr():
        r.rt(1)
    k=0
    while r.fr()-1:
        k+=1
        r.pt('yellow')
        r.dn(1)
    # print(k)
    r.up(1)
    while r.fl():
        r.lt(1)
        r.pt('yellow')
    i=2
    while i<k:
        r.up(1)
        r.pt('yellow')
        i+=1
       
                 
    


r.start(task)

