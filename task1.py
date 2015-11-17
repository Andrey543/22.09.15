import robot
r = robot.rmap()
r.lm('task1')

def task():
    #r.res.config(text='Done')
    r.up(1)
    r.rt(1)
    r.dn(1)
    r.rt(1)
    r.up(1)
    r.rt(1)
    r.dn(1)    
r.start(task)

