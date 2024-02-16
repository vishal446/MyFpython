import pymysql
try:
    conn=pymysql.connect(name="localhost",user="root",db="maharajganj")
    print("connection established")
 mycursor=conn.cursor()
    #que="create table user_info(name varchar(50),age int(3))"
    #que="insert into user_info(name,age)values('Mohan',99)"
    #que="update user_info set name='Shyam' where name='Ram'"
    que="select * from user_info"
    mycursor.execute(que)
    record=mycursor.fetchall()
    print(record)
    for row in record:
        print("Name=",row[0])
        print("Age=", row[1])
    conn.commit() # to save the result(data) of execution of any query
    #print("table Created Successfully")
    print("Data Stored successfully")
    #print("Data Updated  successfully")
except ValueError as e:
    print("Error in connection")
except Exception:
    print("Error in connection")
