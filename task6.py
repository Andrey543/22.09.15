import robot
r = robot.rmap()
r.lm('task1')

def task(): 
    l=int(input())
    h=int(input())
    r.rt(11-l//2)
    i=0
    while i<l:
        r.pt('yellow')
        r.rt(1)
        i+=1
    r.lt(1+l//2)
    i=1
    while i<h:
        r.dn(1)
        r.pt('yellow')
        i+=1
        
r.start(task)

