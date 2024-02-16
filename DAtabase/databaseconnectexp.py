import pymysql
conn=pymysql.connect(host="localhost",user="root",db="maharajganj")
print("connection established")
mycursor=conn.cursor()
# que="insert into user_info(name,age)values('vishal',29)"
que="update user_info set name='vinay' where name='vishu'"
mycursor.execute(que)
conn.commit()
print("table created successfully")
mycursor.close()
conn.close()