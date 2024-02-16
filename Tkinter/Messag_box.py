from tkinter import *
from tkinter import messagebox
root=Tk()
def open_file():
    result=messagebox.askyesnocancel("Save Dialog Box ","Do u want to save File?")
    #result=messagebox.askquestion("Save Dialog Box ","Do u want to save File?")
    print(result)
    if result=='yes':
        print("Your File is Saved")

btn=Button(root,text="Save File",command=open_file)
btn.pack()
root.geometry("400x400+120+120")
root.mainloop()