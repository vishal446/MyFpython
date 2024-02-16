import time
try:
    print("Hello bro, if you want to print from n to m numbers")
    Num1=int(input("Please enter starting number:"))
    Num2=int(input("and enter ending number:"))
    if Num1==0 and Num2==0:
        print("you have enter both value zero!  so here is no any output ")
    elif Num1>Num2:
        print("Welldone!")
        print("Your output are presenting one by one:")
        while Num1>=Num2:
            print(Num1)
            Num1=Num1-1
            time.sleep(1)
    else:
        print("Welldone!")
        print("Your output are presenting one by one:")
        while Num1<=Num2:
            print(Num1)
            Num1=Num1+1
            time.sleep(1)
except ValueError:
    print("Ooh! dear you have entered character, please enter any number!")
except Exception:
    print("Ooh! dear something went wrong, please  check code again!")
print("thank you Dear!")