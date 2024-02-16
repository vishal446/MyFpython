from tkinter import *
import pymysql
from tkinter import messagebox

taz = Tk()
width = taz.winfo_screenwidth()
# print(width)
height = taz.winfo_screenheight()
# print(height)

def dbconfig():
    global conn, mycursor
    conn = pymysql.connect(host="localhost", user="root", db="myhotel")
    mycursor = conn.cursor()


############clear screen#######
def clear_screen():
    global taz
    for widgets in taz.winfo_children():
        widgets.grid.remove()


###########logout############
def logout():
    clear_screen()
    mainheading()
    loginwindow()


def mainheading():
    label = Label(taz, text="Hotel Taz management system", fg="red", bg="yellow", font=("comic sans Ms", 14, "bold"))
    label.grid(row=0, columnspan=4)


usernamevar = StringVar()
passwordvar = StringVar()


def loginwindow():
    usernamevar.set(" ")
    passwordvar.set(" ")

    labellogin = Label(taz, text="Admin login", font=("arial", 15, "bold"))
    labellogin.grid(row=1, columnspan=2)

    usernamelabel = Label(taz, text="user name", font=("arial", 5, "bold"))
    usernamelabel.grid(row=2, column=1)

    passwordlabel = Label(taz, text="user password", font=("arial", 5, "bold"))
    passwordlabel.grid(row=3, column=1)

    usernameEntry = Entry(taz, textvariable=usernamevar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)

    passwordEntry = Entry(taz, show="*", textvariable=passwordvar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton = Button(taz, text="login", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=4, column=1, columnspan=2, padx=20, pady=5)


def welcomewindow():
    clear_screen()
    mainheading()
    welcome = Label(taz, text="welcome Admin", font=("ariel", 25, "bold"))
    welcome.grid(row=1, columnspan=2, padx=50, pady=10)
    logoutButton = Button(taz, text="logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=4, column=1, columnspan = 5)

def adminlogin():
    dbconfig()
    username = usernamevar.get()
    password = passwordvar.get()
    que = "select * from user_info where user_id=%s and user_pass=%s"
    val = (username, password)
    mycursor.execute(que, val)
    data = mycursor.fetchall()
    flag = False
    for row in data:
        flag = True
    conn.close()

    if flag == True:
        welcomewindow()
    else:
        messagebox.showerror("InValid user credential","Either user Name or password is Incorrect")
        usernamevar.set("")
        passwordvar.set("")

taz.title("Hotel Taz Managment System")
mainheading()
loginwindow()
taz.geometry("%dx%d+0+0"%(width, height))
taz.mainloop()