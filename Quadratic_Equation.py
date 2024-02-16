import math
print("To solve the Quadratic Equation! ax^2+bx+c=0")

A_Value=float(input("Enter value of a:"))
B_value=float(input("Enter value of b:"))
C_value=float(input("Enter value of c:"))
Dis= B_value * B_value - 4 * A_Value * C_value
if Dis > 0:
    print("real and different roots!")
elif Dis == 0:
    print(" real and same root!")
else:
    print("Roots are imaginary!")
x_root1 = (-B_value + math.sqrt(Dis)) / (2 * A_Value)
x1_root2 = (-B_value - math.sqrt(Dis))/ (2 * A_Value)
print("the First root of equation x=",x_root1)
print("the second root of equation x1=",x1_root2)

'''
method 2

import math
print("enter the coffecients of quadratic equation")
a=float(input("Enter the value of a"))
b=float(input("Enter the value of b"))
c=float(input("Enter the value of c"))
print("a=",a," b=",b," c=",c)
d=b*b-4*a*c
print("D=",d)
if d==0:
    print("Roots are real and equal")
    x1=-b/(2*a)
    x2=x1
    print("Roots are x1=",x1," x2=",x2)
elif d>0:
    print("Roots are real and unequal")
    x1=(-b+math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are x1=", x1
'''