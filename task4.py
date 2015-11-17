import robot
r = robot.rmap()
r.lm('task1')

def task():
    i1=r.getCoordR()
    i2=r.getCoordC()
    print(i1,i2)
    
    i=1
    while i< i1:
        r.dn(1)
        i+=1
    i=1
    while i< i2:
        r.lt(1)
        i+=1
    i=0
    while i<3:
        j=0
        while j<5:
            r.rt(1)
            r.up(1)
            r.pt('yellow')
            j+=1
        r.dn(3)
        r.lt(5)
        i+=1
        

r.start(task)

