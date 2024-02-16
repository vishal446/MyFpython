# def factorial(n):
#    global p
#    p=1
#    for i in range(1,n+1):
#         p=p*i
#    return p
      
# y=9
# a=factorial(y)
# print(a)

# P,R,T=input('Enter Pricipal, Ratem,Time').split()
# si=(int(P)*int(R)*int(T))/100
# print(si)

# P,R,T=10000,23,4
# c=P*(1+(R/100))**T

# print(c)
# print((P*((1+(R/100))**T))-P)

# num=int(input(":"))
# p=0
# t=num
# while num!=0:
#     print(n)
#     p=p+(n**3)
#     print(p)
#     print(num)
# print(3.14159*(5)**2)

# def prime(n):
#     r=0
#     for i in range(2,n):
#         if n%i==0:
#             r= 1
#             break
        
#     return r
# r=prime(9)
# if r==0:
#     print('prime no')
# else:
#     print('not prime no')

# def fibonacci(n):
#     if n<=0:
#         print('invalid input')
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# l=10
# for i in range(1,l+1):
#     print(fibonacci(i))
# c='j'
# print(ord(c))

import numpy as np

def rotate(arr,l,d):
    pass
arr=np.array([2,3,4,5,6,7,8,9])
d=arr.ndim
print(d)
l=rotate(arr,len(arr),d)