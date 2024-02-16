from tkinter import *
import time
import random
root=Tk()
root.title("Moving ball")
canvas=Canvas(root,width=800,height=600)
canvas.pack()

class Ball:
    def __init__(self,color,size):
        # self.ball = canvas.create_rectangle(10, 10, size, size, fill=color)
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
moving_ball=[]
color=['red','green','orange','gray','blue','yellow']
for i in range(500):
    moving_ball.append(Ball(random.choice(color),random.randrange(50,100)))
while True:
    for j in moving_ball:
        j.animate()
    root.update()
    time.sleep(0.01)
root.geometry("800x600+120+10")
root.mainloop()