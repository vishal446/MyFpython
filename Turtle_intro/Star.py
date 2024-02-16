from turtle import *
t=Turtle()
t.speed(3)
Screen().setup(800,800)
def Star():
    numm = 300
    color_list=['red','blue','yellow','green','black']
    for i in range(54):
        # t.pencolor(color_list[i%5==i])
        t.pensize(10)
        t.pencolor(color_list[i%5])
        t.forward(numm)
        t.right(144)
        numm=numm-5
Star()
done()