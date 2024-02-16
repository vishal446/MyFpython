# try:
#     num=int(input("enter range of fibo-series:"))
#     f_num=0
#     s_num=1
#     i=0
#     while i<=num-1:
#         if i<=1:
#             fibo=i
#             print(fibo)
#         else:
#             fibo=f_num+s_num
#             print(fibo)
#             f_num=s_num
#             s_num=fibo
#         i=i+1
# except ValueError:
#     print("You have entered character not a number. Please enter any number!")
# except Exception:
#     print("Something went wrong!")



# method 2

f_num=int(input("Enter first number:"))
s_num=int(input("Enter second number:"))
num=int(input("enter range of fibo-series:"))
i=3
fib=0
print(f_num," ",s_num)
while i<=num:
    fib=f_num+s_num
    print(fib)
    f_num=s_num
    s_num=fib
    i=i+1
