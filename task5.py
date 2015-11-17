import robot
r = robot.rmap()
r.lm('task1')
def uz():
    r.pt('yellow')
    r.rt(2)
    r.pt('yellow')
    r.dn(1)
    r.lt(1)
    r.pt('yellow')
    r.rt(3)
    r.up(1)
def task():
    uz()
    uz()
    r.lt(8)
    r.dn(3)
    uz()
    uz()

r.start(task)

