'''
What is constructor?
as the name suggest construct something.
constructor is a slpecial member funstion , which can be
invoked(call) automatically , when the object of its class
is created.
'''

class Student:
    def student_info(self):
        print("Name=",self.name,"age=",self.age)

    '''
    def get_data(self,name,age):
        self.name=name
        self.age=age
    '''
    ''' constructor'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("I can when the object is created")

s=Student("Ram",44)  # when object is created constuctor runs
#s.get_data("Ram",44)
s.student_info()
