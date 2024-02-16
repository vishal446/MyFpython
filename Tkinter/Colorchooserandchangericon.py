from tkinter import *
from tkinter import colorchooser
root=Tk()
def color_chooser():
    c=colorchooser.askcolor()
    print(c)
    print(c[0])
    print(c[1])
    root.config(bg=c[1])
root.title("Color chooser")
# root.wm_iconbitmap('notepad.ico')
btn=Button(text="color chooser",command=color_chooser)
btn.pack()
root.geometry("400x400+120+120")
root.mainloop()