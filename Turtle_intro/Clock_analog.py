from turtle import *
import time
time.time()
t=Turtle()
wn=Screen()
t.color("red","white")
t.begin_fill()
t.shape("turtle")
t.end_fill()
wn.title("Simple analog clock")
wn.bgcolor("black")
wn.setup(600,600)
t.speed(0)
t.pensize(3)
t.hideturtle()
wn.tracer(0)

def draw_clock(h,m,s,t):
    t.penup()
    t.goto(0,210)
    t.setheading(180)
    t.pencolor("green")
    t.pendown()
    # t.color("green")
    t.circle(210)
    # draw the clock marking for hand hours
    t.penup()
    t.goto(0,0)
    t.setheading(90)
    for _ in range(12):
        t.forward(190)
        t.pendown()
        t.fd(20)
        t.penup()
        t.goto(0,0)
        t.right(30)
        # draw the clock marking for hand hours
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    for _ in range(60):
        t.forward(200)
        t.pendown()
        t.fd(10)
        t.penup()
        t.goto(0, 0)
        t.right(6)

    # draw no on clock face
    # one
    t.penup()
    t.goto(0,0)
    t.setheading(60)
    t.fd(145)
    t.setheading(0)
    t.fd(15)
    t.pendown()
    t.write(1,move=False, align="center",font=("arial",25,"normal"))

    # two
    t.penup()
    t.goto(0, 0)
    t.setheading(30)
    t.fd(135)
    t.setheading(0)
    t.fd(35)
    t.pendown()
    t.write(2, move=False, align="center", font=("arial", 25, "normal"))

    # Three
    t.penup()
    t.goto(0,0)
    t.setheading(0)
    t.fd(135)
    t.setheading(-30)
    t.fd(45)
    t.pendown()
    t.write(3,move=False,align="center", font=("arial", 25, "normal"))

    #four
    t.penup()
    t.goto(0,0)
    t.setheading(-30)
    t.fd(135)
    t.setheading(-50)
    t.fd(45)
    t.pendown()
    t.write(4,move=False, align="center",font=("arial", 25, "normal"))

    #Five
    t.penup()
    t.goto(0, 0)
    t.setheading(-60)
    t.fd(135)
    t.setheading(-70)
    t.fd(50)
    t.pendown()
    t.write(5, move=False, align="center", font=("arial", 25, "normal"))

    # Six
    t.penup()
    t.goto(0, 0)
    t.setheading(-90)
    t.fd(135)
    t.setheading(-90)
    t.fd(50)
    t.pendown()
    t.write(6, move=False, align="center", font=("arial", 25, "normal"))

    # Seven

    t.penup()
    t.goto(0, 0)
    t.setheading(-120)
    t.fd(135)
    t.setheading(-105)
    t.fd(50)
    t.pendown()
    t.write(7, move=False, align="center", font=("arial", 25, "normal"))

    #Eight

    t.penup()
    t.goto(0, 0)
    t.setheading(-150)
    t.fd(135)
    t.setheading(-130)
    t.fd(45)
    t.pendown()
    t.write(8, move=False, align="center", font=("arial", 25, "normal"))

    # Nine

    t.penup()
    t.goto(0, 0)
    t.setheading(-180)
    t.fd(135)
    t.setheading(-155)
    t.fd(35)
    t.pendown()
    t.write(9, move=False, align="center", font=("arial", 25, "normal"))

    # Ten
    t.penup()
    t.goto(0, 0)
    t.setheading(-210)
    t.fd(135)
    t.setheading(-180)
    t.fd(20)
    t.pendown()
    t.write(10, move=False, align="center", font=("arial", 25, "normal"))

    # Elevan

    t.penup()
    t.goto(0, 0)
    t.setheading(-240)
    t.fd(135)
    t.setheading(-205)
    t.fd(18)
    t.pendown()
    t.write(11, move=False, align="center", font=("arial", 25, "normal"))

    # Twelve

    t.penup()
    t.goto(0, 0)
    t.setheading(-270)
    t.fd(145)
    t.setheading(-220)
    t.fd(0)
    t.pendown()
    t.write(12, move=False, align="center", font=("arial", 25, "normal"))

    # draw hour hand
    t.pu()
    t.goto(0,0)
    t.pencolor("red")
    t.setheading(90)
    angle=(h/12)*360
    t.rt(angle)
    t.pendown()
    t.fd(80)

    # draw minute hand
    t.pu()
    t.goto(0, 0)
    t.pencolor("Blue")
    t.setheading(90)
    angle = (m / 60) * 360
    t.rt(angle)
    t.pendown()
    t.fd(120)

    # draw second hand
    t.pu()
    t.goto(0, 0)
    t.pencolor("yellow")
    t.setheading(90)
    angle = (s / 60) * 360
    t.rt(angle)
    t.pendown()
    t.fd(160)

    # Designed by
    t.penup()
    t.goto(0,0)
    t.pencolor("gold")
    t.setheading(268)
    t.fd(125)
    t.setheading(0)
    t.fd(5)
    t.pendown()
    t.write("Designed by Vishal",move=False,align="center",font=("arial",10,"normal"))
while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))
    draw_clock(h,m,s,t)
    wn.update()
    time.sleep(1)
    t.clear()
mainloop()
