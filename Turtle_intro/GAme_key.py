from turtle import *
t=Turtle()

def up():
    t.forward(100)

def down():
    t.backward(200)

def right():
    t.right(90)
    t.forward(100)

def left():
    t.left(90)
    t.forward(100)

w=Screen()
w.onkey(up,"Up")
w.onkey(down,"Down")
w.onkey(left,"Left")
w.onkey(right,"R")
w.listen()

done()