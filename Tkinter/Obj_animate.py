from tkinter import *
import time
import random
root=Tk()
root.title("Moving ball")
canvas=Canvas(root,width=800,height=600)
canvas.pack()

class Ball:
    def __init__(self,color,size):
        self.ball = canvas.create_oval(10, 10, size, size, fill=color)
        self.xspeed = random.randrange(1,8)
        self.yspeed = random.randrange(1,8)

    def animate(self):
        canvas.move(self.ball, self.xspeed, self.yspeed)
        pos = canvas.coords(self.ball)
        if pos[3] >= 600 or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= 800 or pos[0] <= 0:
            self.xspeed = -self.xspeed
ball1=Ball("green",50)

ball2=Ball("orange",100)

ball3=Ball("blue",140)
while True:
    ball1.animate()
    ball2.animate()
    ball3.animate()
    root.update()
    time.sleep(0.001)
root.geometry("800x600+120+10")
root.mainloop()