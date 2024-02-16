from array import *

marks=array('i',[]) # to create an empty array
n=int(input("How many students marks u want to store"))
print("No of students=",n)

for i in range(n):
    x=int(input("Enter the marks of student"))
    marks.append(x)

print(marks)
Num=int(input("Enter a number to search:"))
for j in marks:
    if x[j]==Num:
        print("number found")
    else:
        print("not found")

