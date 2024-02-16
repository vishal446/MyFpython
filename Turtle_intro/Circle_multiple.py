from turtle import *
t=Turtle()
t.up()
t.goto(200,0)
color_list=['red','yellow','green','blue']
for i in range(4):
    t.down()
    t.pensize(10)
    t.color(color_list[i])
    t.circle(50)
    t.up()
    t.backward(100)
done()