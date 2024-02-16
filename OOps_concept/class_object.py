class Student:
    def student_info(self):
        print("vishal",16)

# how to create object
ob=Student()
print(type(ob))

Student.student_info(ob) #accessing data from function

# but we can access like it
ob.student_info()

a=5
print(type(a))