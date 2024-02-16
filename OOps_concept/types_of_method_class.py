'''
types of method
1. instance method -- Which accepts self as parameter
     (a). Accessor Method -only fetch the value
     (b). Mutator Method  - Set the value
2. class method  --- which accepts cls as parameter

3. static method-- which accepts no parameter

'''

class Student:
    school='techsrijan'  # class variable


    @classmethod    # decorator
    def get_school(cls):
        return cls.school

    def __init__(self,m1,m2,m3):   # instance method
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def get_m2(self):  # instance--accessor --fetch
        return (self.m2)

    def set_m2(self): # instance --mutator --set
        self.m2=500

    @staticmethod
    def msg():  # static method --no parameter
        print("This is static method")


#static -method  --classname.method()
Student.msg()
# class method --classname.method()
print(Student.get_school())
'''
amit=Student(10,20,30)
amit.set_m2()
print(amit.get_m2())
'''