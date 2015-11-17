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
    min=40
    while i<13:
        s=0    
        while j<9:
            s=0 
            s=s+int(r.gettext())
            r.rt(1)
            s=s+int(r.gettext())
            r.dn(1)
            s=s+int(r.gettext())
            r.lt(1)
            s=s+int(r.gettext())
            r.up(1)
            if s<=min:
                i1=r.getCoordR()
                i2=r.getCoordC() 
                min=s
            j+=1
            r.dn(1)
        r.up(9)
        j=0
        i+=1   
        r.rt(1)  
    print(i1,i2)   
    r.dn(i1-1)
    r.lt(14-i2) 
    r.pt('yellow')
    r.rt(1)
    r.pt('yellow')
    r.dn(1)
    r.pt('yellow')
    r.lt(1)
    r.pt('yellow')
                   
r.start(task)

