'''
type of variable:
    1. class variable and static variable
    2. instance variable  -- ariable declared inside of function
'''
class Car:
    wheel=8  #class variable
    def __init__(self):
        print("this is a car")
        self.milage=86      #instance variable
        self.name='BMW'     #instance varible

# __init__(self) automatically calls the function
c1=Car()
c2=Car()
c3=Car()
# print(c1.wheel,c2.name,c3.milage)

# if we want to change value of car

c1.wheel=4
c2.name='tata'
c3.milage=100
print(c1.wheel,c2.name,c3.milage)