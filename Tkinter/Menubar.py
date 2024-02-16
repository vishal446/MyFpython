from tkinter import *
root=Tk()

def msg():
    print("hi")
root.title("Menubar tutorial")

main_menu=Menu(root)
root.config(menu=main_menu)
file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="FILE",menu=file_menu)
file_menu.add_command(label="New",accelerator="Ctrl+N",command=msg)
file_menu.add_command(label="Open",accelerator="Ctrl+O")
file_menu.add_separator()
# creating submenu
save_menu=Menu(file_menu,tearoff=False)
file_menu.add_cascade(label="Save",menu=save_menu)
save_menu.add_command(label="Save Now")
save_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)

# creating Editmenu
edit_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Copy",accelerator="Ctrl+C")
edit_menu.add_command(label="Paste",accelerator="Ctrl+P")
root.geometry("600x500+120+120")
root.mainloop()