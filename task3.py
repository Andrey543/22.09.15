import robot
r = robot.rmap()
r.lm('task1')

def task():
    r.rt(1)
    i=0
    while i<=2:
        r.rt(1)
        r.dn(1)
        r.up(1)
        r.rt(1)
        i+=1
    r.rt(1)

r.start(task)

