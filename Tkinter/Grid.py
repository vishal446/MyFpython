from tkinter import *
root=Tk()

label=Label(root,text="Enter first number:",bg="red",fg="black",font=('Comic Sans Ms',15,'bold'))
label.grid(row=0,column=0)
first=IntVar()

txt=Entry(root,font=("Comic Sans Ms",15,"bold"),textvariable=first)
txt.grid(row=0,column=1)

label1=Label(root,text="Enter second NUmber:",bg='red',fg="black",font=("Comic Sans Ms",15,"bold"))
label1.grid(row=1,column=0)

second=IntVar()
txt=Entry(root,font=("Comic Sans Ms",15,"bold"))
txt.grid(row=1,column=1)

btn=Button(root,text="Add",font=("Comic Sans Ms",15,"bold"))
btn.grid(row=2,columnspan=2)

third=IntVar()
txt1=Entry(root,font=("Comic Sans Ms",15,"bold"),textvariable=third)
txt1.grid(row=3,column=3)
root.geometry("400x400+150+100")
root.mainloop()

