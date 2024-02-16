from numpy import *
arr=array([1,2,3,4,5])
print("arr=",arr , "id of arr=",id(arr))

# aliasing
arr2=arr  # assign the value of one array into another
print("arr2=",arr2,"id of arr2=",id(arr2))

arr[0]=500
print("arr=",arr , "id of arr=",id(arr))
print("arr2=",arr2,"id of arr2=",id(arr2))


#shallow copy
# what if i want to create two different array i.e. two diffrent
# memory address

arr3=array([3,5,6,3,77,88])
print("arr3=",arr3,"id of arr3=",id(arr3))

arr4=arr3.view()
print("arr4=",arr4 , "id of arr4=",id(arr4))

arr3[2]=5658666
print("arr3=",arr3,"id of arr3=",id(arr3))
print("arr4=",arr4 , "id of arr4=",id(arr4))


#deep copy
# if i want two diffrenent memory address and changes on one does not
# affect other

arr5=[3,77,22,99,333,000,55]
print("arr5=",arr5,"id of arr5=",id(arr5))

arr6=arr5.copy()
print("arr6=",arr6,"id of arr6=",id(arr6))

arr5[0]=800
print("arr5=",arr5,"id of arr5=",id(arr5))
print("arr6=",arr6,"id of arr6=",id(arr6))