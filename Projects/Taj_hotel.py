from tkinter import *
import pymysql
import mysql.connector
from tkinter import messagebox,filedialog
from tkinter import ttk
from datetime import datetime


taz=Tk()
width=taz.winfo_screenwidth()
# print(width)
height=taz.winfo_screenheight()
# print(height)

tazTV=ttk.Treeview(height=10,column=("Item Name""Rate","Type"))
tazTV1=ttk.Treeview(height=10,column=("Date""Name","Type","Rate","Total"))

# for char input()
def only_char_input(P):
    if P.isalpha() or P=='':
        return True
    return False

callback=taz.register(only_char_input)
# for digit
def only_numeric_input(P):
    if P.isdigit() or P=='':
        return True
    return False
callback2=taz.register(only_numeric_input)


######### Databse connection ########

def dbconfig():
    global conn,mycursor
    conn=pymysql.connect(host="localhost",user="root",passwd='Admin@123',db="tajproject")
    mycursor=conn.cursor()

##################clear screen########

def clear_screen():
    global taz
    for widgets in taz.winfo_children():
        widgets.grid_remove()

############log out###########

def logout():
    clear_screen()
    mainheading()
    loginwindow()


def mainheading():
    label=Label(taz,text="Hotel Taz Management System",fg="red",bg="yellow"
                ,font=("Comic Sans Ms",40,"bold"),padx=300,pady=0)
    label.grid(row=0,columnspan=4)
usertext=StringVar()
userpass=StringVar()
def loginwindow():
    labellogin=Label(taz,text="Admin login",font=("arial",25,"bold"))
    labellogin.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

    usernamelabel=Label(taz,text="User Name",font=("arial",15,"bold"))
    usernamelabel.grid(row=2,column=1,padx=20,pady=5)

    passwordlabel=Label(taz,text="Password",font=("arial",15,"bold"))
    passwordlabel.grid(row=3,column=1,padx=20,pady=5)

    usernametext=Entry(taz,textvariable=usertext)
    usernametext.grid(row=2,column=2,padx=20,pady=5)

    userpassword=Entry(taz,show="*",textvariable=userpass)
    userpassword.grid(row=3,column=2,padx=20,pady=5)

    loginbtn=Button(taz,text="Login",width=20,height=2,fg="green",bd=10,command=adminlogin)
    loginbtn.grid(row=4,column=1,columnspan=2,padx=20,pady=5)



####### back button ########

def back():
    clear_screen()
    mainheading()
    welcomwidndow()
###########################
def getitemInTreeview():
    # to delete already inserted data
    records=tazTV.get_children()
    for x in records:
        tazTV.delete(x)

    conn=pymysql.connect(host="localhost",user="root",passwd='Admin@123',db="tajproject")
    mycursor=conn.cursor(pymysql.cursors.DictCursor)
    # print(mycursor)
    query1="select * from item"
    mycursor.execute(query1)
    data=mycursor.fetchall()
    # print(data)
    for row in data:
        tazTV.insert('','end',text=row['item_name'],values=(row["item_rate"],row["item_type"]))
    conn.close()
    tazTV.bind("<Double-1>",OnDoubleClick)

#########double click##############
def OnDoubleClick(event):
    item=tazTV.selection()
    itemNameVar1=tazTV.item(item,"text")
    item_detail=tazTV.item(item,"values")
    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemtypeVar.set(item_detail[1])

#############update item###########
def updateItem():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    que="update item set item_rate=%s,item_type=%s where item_name=%s"
    val=(rate,type,name)
    mycursor.execute(que,val)
    conn.commit()
    messagebox.showinfo("Updation confirmation","Item Updated Successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getitemInTreeview()

###########delete item##########
def deleteItem():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemtypeVar.get()
    dbconfig()
    que1 = "delete from item where item_name=%s"
    val = (name)
    mycursor.execute(que1, val)
    conn.commit()
    messagebox.showinfo("Deletion confirmation", "Item Deleted Successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getitemInTreeview()
##############Bill Window##########
global x
x=datetime.now()
datetimeVar=StringVar()
datetimeVar.set(x)

mobileVar=StringVar()
custumerNameVar=StringVar()
combovariable=StringVar()
baserate=StringVar()
cost=StringVar()
qtyvariable=StringVar()

############## combo data ############
def combo_input():
    dbconfig()
    mycursor.execute('select item_name from item')
    data=[]
    for row in mycursor.fetchall():
        data.append(row[0])
    return data
##########optionCallBack############
def optionCallBack(*args):
    global itemname
    itemname=combovariable.get()
    # print(itemname)
    aa=ratelist()
    # print(aa)
    baserate.set(aa)
    global v
    for i in aa:
        for j in i:
            v=j


###############opetionCallBack1##########
def optionCallBack1(*args):
    global qty
    n=int(v)
    qty=qtyvariable.get()
    n1=int(qty)
    final=n*n1
    cost.set(final)



##########rate list################
def ratelist():
    dbconfig()
    que2="select item_rate from item where item_name=%s"
    val=(itemname)
    mycursor.execute(que2,val)
    data=mycursor.fetchall()
    print(data)
    return data


#############################################
def billWindow():
    clear_screen()
    mainheading()
    Billitem = Label(taz, text="Generate Bill", font=("arial", 25, "bold"))
    Billitem.grid(row=1, column=1, columnspan=2, padx=50, pady=10)
    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=2, command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1)

    backButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=2, command=back)
    backButton.grid(row=4, column=0, columnspan=1)

    printButton = Button(taz, text="Print Bill", width=20, height=2, fg="green", bd=2, command=printBill)
    printButton.grid(row=5, column=0, columnspan=1)

    dateTiemLabel=Label(taz,text="Date & Time",font=("arial",20,"bold"))
    dateTiemLabel.grid(row=2,column=1,padx=20,pady=5)

    dateTimeEntry=Entry(taz,font=("arial",20,"bold"),textvariable=datetimeVar)
    dateTimeEntry.grid(row=2,column=2,padx=20,pady=5)

    custumerNameLabel = Label(taz, text="Customer Name", font=("arial", 15, "bold"))
    custumerNameLabel.grid(row=3, column=1, padx=20, pady=5)

    custumerNameEntry = Entry(taz, font=("arial", 15, "bold"), textvariable=custumerNameVar)
    custumerNameEntry.grid(row=3, column=2, padx=20, pady=5)
    custumerNameEntry.configure(validate="key", validatecommand=(callback, "%P"))

    mobileLabel = Label(taz, text="Contact No", font=("arial", 15, "bold"))
    mobileLabel.grid(row=4, column=1, padx=20, pady=5)

    mobileEntry = Entry(taz, font=("arial", 15, "bold"), textvariable=mobileVar)
    mobileEntry.grid(row=4, column=2, padx=20, pady=5)
    mobileEntry.configure(validate="key", validatecommand=(callback2, "%P"))

    selectLabel = Label(taz, text="Select Item", font=("arial", 15, "bold"))
    selectLabel.grid(row=5, column=1, padx=20, pady=5)
    # selectEntry = Entry(taz, font=("arial", 15, "bold"), textvariable=mobileVar)
    # selectEntry.grid(row=4, column=2, padx=20, pady=5)

    l=combo_input()
    c=ttk.Combobox(taz,value=l,textvariable=combovariable,font=("arial", 15, "bold"))
    c.set("select Item")
    combovariable.trace('w',optionCallBack)
    c.grid(row=5,column=2,padx=20,pady=5)
    rateLabel = Label(taz, text="Item Rate", font=("ariel", 15, "bold"))
    rateLabel.grid(row=6, column=1, padx=20, pady=5)

    rateEntry = Entry(taz, font=("ariel", 15, "bold"), textvariable=baserate)
    rateEntry.grid(row=6, column=2, padx=20, pady=5)
    qtyLabel = Label(taz, text="Select Quantity", font=("arial", 15, "bold"))
    qtyLabel.grid(row=7, column=1, padx=20, pady=5)

    global qtyvariable
    l2 = [1,2,3,4,5]
    qty = ttk.Combobox(taz, value=l2, textvariable=qtyvariable, font=("arial", 15, "bold"))
    qty.set("select Quantity")
    qtyvariable.trace('w',optionCallBack1)
    qty.grid(row=7, column=2, padx=20, pady=5)

    costLabel = Label(taz, text="Cost", font=("ariel", 15, "bold"))
    costLabel.grid(row=8, column=1, padx=20, pady=5)

    costEntry = Entry(taz, textvariable=cost,font=("ariel", 15, "bold"))
    costEntry.grid(row=8, column=2, padx=20, pady=5)

    billButton=Button(taz,text="Save bill",font=("ariel",15,"bold"),width=10,height=2,bg="yellow",fg="blue",bd=5,command=saveBill)
    billButton.grid(row=9,column=2,padx=20,pady=5)

#######################
#########saveBill#########
def saveBill():
    dt=datetimeVar.get()
    customer_name=custumerNameVar.get()
    mobile=mobileVar.get()
    item_name=itemname
    item_rate=v
    item_qty=qtyvariable.get()
    total=cost.get()
    dbconfig()
    insque="insert into bill_gen(datetime,customer_name,contact_no,item_name,item_rate,item_qty,cost)" \
           "values(%s,%s,%s,%s,%s,%s,%s)"
    val=(dt,customer_name,mobile,item_name,item_rate,item_qty,total)
    mycursor.execute(insque,val)
    conn.commit()
    messagebox.showinfo("Save Data","Bill Saved successfully")
    custumerNameVar.set("")
    itemnameVar.set("")
    cost.set("")
###########print Bill#########
def printBill():
    clear_screen()
    mainheading()
    printitem = Label(taz, text="Bill Details", font=("arial", 25, "bold"))
    printitem.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=2, command=logout)
    logoutButton.grid(row=1, column=0, columnspan=1)

    backButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=2, command=back)
    backButton.grid(row=1, column=3, columnspan=1)

    clickButton = Button(taz, text="Double Click to Treeview To print Bill", font=("arial", 25, "bold"))
    clickButton.grid(row=2, column=1, columnspan=3, padx=50, pady=10)

    # treview
    tazTV1.grid(row=4, column=0, columnspan=4)
    style = ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview",bg="yellow", feildbackground="green")
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV1.yview)
    scrollBar.grid(row=5, column=5, sticky="NSE")

    tazTV1.configure(yscrollcommand=scrollBar.set)
    tazTV1.heading('#0', text='Date/Time')
    tazTV1.heading('#1', text='Name')
    tazTV1.heading('#2', text='Mobile')
    tazTV1.heading('#3', text='Selected Food')
    tazTV1.heading('#4', text='Total Cost')
    displaybill()
################Double click####################3
def OnDoubleClick2(event):
    print('Double OnDoubleClick')
    item = tazTV1.curselection()
    global itemNameVar11
    itemNameVar11= tazTV1.item(item, "text")
    item_detail1 = tazTV1.item(item, "values")
    print('befor receipt')
    receipt()

###################################

#########display bill##############
def displaybill():
    # to delete already inserted data
    records = tazTV1.get_children()
    for x in records:
        tazTV1.delete(x)

    conn = pymysql.connect(host="localhost", user="root", password='Admin@123', db="tajproject")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    # print(mycursor)
    query1 = "select * from bill_gen"
    mycursor.execute(query1)
    data = mycursor.fetchall()
    # print(data)
    for row in data:
        tazTV1.insert('', 'end', text=row["datetime"], values=(row['customer_name'], row['contact_no'], row['item_name'],row['item_rate'],row['item_qty'],row['cost']))
    conn.close()
    print("binding")
    tazTV1.bind("<Double-Button-1>",OnDoubleClick2)

####################################
##########receipt

def receipt():
    billstring=""
    print('receipt')
    billstring+="=============== My Hotel Bill ==============\n\n"
    billstring+="=============== Customer Detail ==============\n\n"

    dbconfig()
    query="select * from bill_gen where datetime='{}';".format(itemNameVar11)
    mycursor.execute(query)
    data=mycursor.fetchall()
    for row in data:
        billstring+="{}{:<20}{:<10}\n".format("Customer Name","",row[1])
        billstring+="{}{:<20}{:<10}\n".format("Date/Time","",row[2])
        billstring+="{}{:<20}{:<10}\n".format("Contact no","",row[3])
        billstring+="\n=============Item Datail ==============\n"
        billstring+="{:<10}{:<10}{:<15}{:<15}".format("item Name","Rate","Quantity","Total Cost")
        billstring+="\n{:<10}{:<10}{:<25}{:<25}".format(row[4],row[5],row[6],row[7])
        billstring+="==========================================\n"
        billstring+="{}{:<10}{:<15}{:<10}\n".format("Totel Cost"," "," ",row[7])
        billstring+="\n\n =============Thanks Please Visit Again============\n"


    bilFile=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if bilFile is None:
        messagebox.showerror("File Name Error","Invalid File Name")
    else:
        bilFile.write(billstring)
        bilFile.close()



############################3###########

itemtypeVar=StringVar()
itemnameVar=StringVar()
itemrateVar=StringVar()
def addItemWindow():
    clear_screen()
    mainheading()
    addition=Label(taz,text="Insert item",font=("arial",25,"bold"))
    addition.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

    itemnameLabel=Label(taz,text="Item Name",font=("arial",20,"bold"))
    itemnameLabel.grid(row=2,column=1,padx=20,pady=5)

    itemrateLabel=Label(taz,text="Item Rate",font=("arial",20,"bold"))
    itemrateLabel.grid(row=3,column=1,padx=20,pady=5)

    itemtypeLabel=Label(taz,text="Item Type",font=("arial",20,"bold"))
    itemtypeLabel.grid(row=4,column=1,padx=20,pady=5)

    itemnameEntry=Entry(taz,textvariable=itemnameVar)
    itemnameEntry.grid(row=2,column=2,padx=20,pady=5)
    # for validation
    itemnameEntry.configure(validate="key",validatecommand=(callback,"%P"))

    itemrateEntry=Entry(taz,textvariable=itemrateVar)
    itemrateEntry.grid(row=3,column=2,padx=20,pady=5)
    itemrateEntry.configure(validate="key", validatecommand=(callback2, "%P"))

    itemtypeEntry=Entry(taz,textvariable=itemtypeVar)
    itemtypeEntry.grid(row=4,column=2,padx=20,pady=5)
    itemtypeEntry.configure(validate="key", validatecommand=(callback, "%P"))

    additem=Button(taz,text="Add Item",width=20,height=2,fg="green",bd=10,command=addItem)
    additem.grid(row=3,column=3,columnspan=1)

    updateitem = Button(taz, text="Update Item", width=20, height=2, fg="green", bd=10, command=updateItem)
    updateitem.grid(row=4, column=3, columnspan=1)

    deleteitem = Button(taz, text="Delete Item", width=20, height=2, fg="green", bd=10, command=deleteItem)
    deleteitem.grid(row=5, column=3, columnspan=1)

    logoutButton=Button(taz,text="Logout",width=20,height=2,fg="green",bd=2,command=logout)
    logoutButton.grid(row=3,column=0,columnspan=1)

    backButton=Button(taz,text="Back",width=20,height=2,fg="green",bd=2,command=back)
    backButton.grid(row=4,column=0,columnspan=1)

    # treview
    tazTV.grid(row=8,column=0,columnspan=3)
    style=ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview",feildbackground="green")
    scrollBar=Scrollbar(taz,orient="vertical",command=tazTV.yview)
    scrollBar.grid(row=8,column=2,sticky="NSE")

    tazTV.configure(yscrollcommand=scrollBar.set)
    tazTV.heading('#0',text='Item Name')
    tazTV.heading('#1',text='Rate')
    tazTV.heading('#2',text='Type')

    getitemInTreeview()

def addItem():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    query="insert into item(item_name,item_rate,item_type)values(%s,%s,%s)"
    val=(name,rate,type)
    mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo("Save Item","Item Saved successfully")
    itemnameVar.set("")
    itemtypeVar.set("")
    itemrateVar.set("")
    getitemInTreeview()

def welcomwidndow():
    clear_screen()
    mainheading()
    welcome=Label(taz,text="Welcome Admin",font=("arial",25,"bold"))
    welcome.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

    logoutbtn = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutbtn.grid(row=4, column=1, columnspan=2, padx=20, pady=5)

    manageRest=Button(taz,text="Manage Hotel",width=20,height=2,fg="green",bd=2,command=addItemWindow)
    manageRest.grid(row=5,column=1,columnspan=2,padx=20,pady=5)

    BillGen = Button(taz, text="Bill Generation", width=20, height=2, fg="red", bd=10, command=billWindow)
    BillGen.grid(row=6, column=1, columnspan=2, padx=20, pady=5)


def adminlogin():
    dbconfig()
    username=usertext.get()
    pasword=userpass.get()
    que="select * from taj_datainfo where user_id=%s and password=%s"
    val=(username,pasword)
    mycursor.execute(que,val)
    data=mycursor.fetchall()
    flag=False
    for row in data:
        flag=True
    conn.close()

    if flag==True:
        welcomwidndow()
    else:
        messagebox.showerror("Invalid User Credential","Either User Name or Password is Incorrect")
        usertext.set("")
        userpass.set("")


mainheading()
loginwindow()
taz.title("Hotel Taz Management System")
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()