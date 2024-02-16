from math import *
s=sqrt(36)
print(s)


'''
function should not return any value
function should return value
function should not recieve any argument/parameter
function should take parameter

'''
def add():
    #x,y=2,10
    x=int(input("enter first number"))
    y = int(input("enter second number"))
    c=x+y
    print("Add=",c)

#add()
#add()
def add1():
    #x,y=2,10
    x=int(input("enter first number"))
    y = int(input("enter second number"))
    c=x+y
    d=x-y
    return c,d

#s,t=add1()
#print(s,t)
def multi(x,y):  # here x and y are called formal argument
    m=x*y
    print(m)

a=int(input("enter first number"))
b=int(input("enter second number"))
multi(5,6)
multi(a,b)  # here a and b are called actual argument


def sub(x,y):  # here x and y are called formal argument
    d=x//y
    return d

div=sub(50,5)
print(div)