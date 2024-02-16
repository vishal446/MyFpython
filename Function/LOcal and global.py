# identification of local and global variable
# method 1
# a=20 #global variable
# def msg():
#     x=50  #local variable
#     print("x=",x)
#     print("a=",a)
# print("a=",a)
# msg()
# print("a=",a)
# print("a=",a)

# method 2
# if we want to declare variable in function
# def msg():
#     # global a
#     global a
#     a=90
#     print("a=", a)
# msg()
# print("a=",a)


# method 3
# x=20
# def msg():
#     x=50
#     print("x=",x)
#     d=globals()['x']
#     print("x=",d)
# msg()