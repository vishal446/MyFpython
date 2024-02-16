
from turtle import *
t=Turtle()
Screen().setup(1000,600)
t.penup()
t.forward(150)
t.pendown()
t.shape("turtle")
def Olympic():
    Color_list = ["red", "black","blue"]
    for i in range(3):
        t.color(Color_list[i])
        t.pensize(5)
        t.circle(50)
        t.penup()
        t.backward(110)
        t.pendown()
    Color_list1=["yellow","green"]
    for i in range(2):
        t.color(Color_list1[i])
        # t.color("col")
        t.pensize(5)
        t.penup()
        t.forward(110)
        t.left(90)
        t.forward(5)
        t.pendown()
        t.circle(-50)
        t.penup()
        t.backward(5)
        t.right(90)
        t.pendown()
Olympic()
done()