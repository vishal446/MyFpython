from tkinter import *
from tkinter import filedialog,messagebox,colorchooser

class MyNotePad:
    current_file="no-file"

    def change_back_color(self):
        c=colorchooser.askcolor()
        self.txt_area.configure(background=c[1])

    def change_fore_color(self):
        c=colorchooser.askcolor()
        self.txt_area.configure(foreground=c[1])

    def exit_file(self):
        s=self.txt_area.get(1.0,END)
        if not s.strip():
            quit()
        else:
            result=messagebox.askyesnocancel("Save Dialog Box","Do you want save?")
            if result==True:
                self.save_as_file()
            elif result==False:
                quit()

    def clear(self):
        self.txt_area.delete(1.0,END)


    def new_file(self):
        s=self.txt_area.get(1.0,END)
        if not s.strip():
            pass
        else:
            result=messagebox.askyesnocancel("Save Dialog Box","Do you to save this file?")
            if result==True:
                self.save_as_file()
                self.clear()
            elif result==False:
                self.clear()
    def save_as_file(self):
        f=filedialog.asksaveasfile(mode="w",defaultextension="*.txt")
        data=self.txt_area.get(1.0,END)
        f.write(data)
        self.current_file=f.name
        f.close()
    def save_file(self):
        if self.current_file=="no-file":
            self.save_as_file()
        else:
            f=open(self.current_file,mode="w")
            f.write(self.txt_area.get(1.0,END))


    def open_file(self,event=""):
        result=filedialog.askopenfile(initialdir="/",title="Open file",
        filetypes=(("Text File","*.txt"),("All File","*.*")))
        # print(result)
        for data in result:
            self.txt_area.insert(INSERT,data)
        self.current_file=result.name


    def copy_file(self):
        self.txt_area.clipboard_clear()
        self.txt_area.clipboard_append(self.txt_area.selection_get())

    def paste_file(self):
        self.txt_area.insert(INSERT,self.txt_area.clipboard_get())

    def cut_file(self):
        self.copy_file()
        self.txt_area.delete('sel.first','sel.last')

    def del_file(self):
        self.txt_area.delete('sel.first','sel.last')

    def __init__(self,master):
        self.master=master
        master.title("My Note pad")
        master.bind("<Control-o>",self.open_file)
        master.bind("<Control-O>",self.open_file)
        # master.wm_iconbitmap("notepad.ico") #showing wrong
        self.txt_area=Text(master,padx=5,pady=5,wrap=WORD,
        selectbackground="red",bd=2,insertwidth=3,undo=True)
        self.txt_area.pack(fill=BOTH,expand=1)


        self.main_menu=Menu()
        self.master.config(menu=self.main_menu)

        #creating file menu
        self.file_menu=Menu(self.main_menu,tearoff="False")
        self.main_menu.add_cascade(label="FILE",menu=self.file_menu)
        self.file_menu.add_command(label="New",accelerator="Ctrl+n",command=self.new_file)
        self.file_menu.add_command(label="Open",accelerator="Ctrl+o",command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save",command=self.save_file)
        self.file_menu.add_command(label="Save as",command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.exit_file)

        ##########################
        # creating Edit menu
        self.edit_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="EDIT",menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo",accelerator="Ctrl+z",command=self.txt_area.edit_undo)
        self.edit_menu.add_command(label="Redo",accelerator="Ctrl+y",command=self.txt_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut",accelerator="Ctrl+x",command=self.cut_file)
        self.edit_menu.add_command(label="Copy",accelerator="Ctrl+c",command=self.copy_file)
        self.edit_menu.add_command(label="Paste",accelerator="Ctrl+p",command=self.paste_file)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Delete",accelerator="Ctrl+del",command=self.del_file)

        ##########################
        # creating Format menu
        self.format_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="FORMAT",menu=self.format_menu)
        self.format_menu.add_command(label="Background color",command=self.change_back_color)
        self.format_menu.add_command(label="ForeGround color",command=self.change_fore_color)
        # self.format_menu.add_command(label=)




root=Tk()
b=MyNotePad(root)
root.mainloop()