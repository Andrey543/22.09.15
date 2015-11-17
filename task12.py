import robot
r = robot.rmap()
r.lm('task1')

def task():
    while (r.fu()-1)or(r.fl()-1)or(r.fr()-1):
        if ((r.fu()-1)and(r.fl()-1))or((r.fu()-1)and(r.fr()-1)):
            r.pt('yellow')
        if (r.fu()-1)and(r.fl()):
            r.lt(1)
        if (r.fl()-1)and(r.fr()-1):
            r.up(1)
        if r.fl()-1:  
            r.dn(1) 
        if r.fr()-1:
            r.up(1)
        if(r.fl())and(r.fr())and(r.fu()):
            r.lt(1)
            while r.fu()-1:
                r.lt(1)
            r.up(1)             

r.start(task)

