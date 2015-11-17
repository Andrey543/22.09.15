import robot
r = robot.rmap()
r.lm('task1')

def task():
	i=0
	while i<=4:
	    r.up(1)
	    r.pt('yellow')
	    r.up(1)
	    r.rt(1)
	    r.pt('red')
	    r.dn(2)
	    r.pt()
	    r.rt(1)
	    r.up(1)
	    r.pt('blue')
	    r.dn(1)
	    r.rt(1)

r.start(task)

