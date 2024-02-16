from tkinter import *

root=Tk()
root.title("This is my first tkinter windows title")
# funtion
def msg():
    print("Good morning")

def msg2():
    print("Good afernoon")
label=Label(root,text="Enter Number:",bg='red',fg='yellow',font=
('Comic Sans Ms',20,'bold'))
label.pack(side=TOP)
#label1.pack(side=LEFT)
label1=Label(root,text="Enter your father name:",bg='red',fg='yellow',
             font=('Comic Sans Ms',20,'bold'))
label1.pack(side=BOTTOM)

btn=Button(root,text="Click me",bg='blue',fg='yellow',
           font=("Comic Sans Ms",20,"bold"),command=msg)
btn.pack()

btn1=Button(root,text="Msg me",bg="yellow",fg='red',
            font=("Comic Snas Ms",20,"bold"),command=msg2)
btn1.pack(fill=X)

txt=Entry(root,font=("Comic Sans Ms",20,"bold"))
txt.pack()

btn3=Button(root,text="Exit",font=("Comic Sans Ms",20,"bold"),command=quit)
btn3.pack()

root.resizable(0,0)
root.geometry("400x400+300+100")
root.mainloop()

