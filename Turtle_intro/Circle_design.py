from turtle import *
t=Turtle()
w=Screen()
Screen().setup(1000,600)
# t.circle(100) #anti clock wise
# t.undo()
# t.circle(-100) #clock wise
# t.undo()
# t.reset()
t.circle(100,steps=12)
t.circle(-70,extent=180)
t.write("this is doneby me!",font=15)

t.up()
t.goto(200,300)
t.down()
t.circle(100)
done()