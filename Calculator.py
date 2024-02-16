try:
    print("Enter two numbers!")
    Num1=float(input("first number:"))
    Num2=float(input("second number:"))
    print("Press 1 : Addition ,","Press 2 : Subtraction ,","Press 3 : Multiplication ,","Press 4 : Division")
    Choice=int(input("Please enter your choice:"))
    if Choice==1:
        Add=Num1+Num2
        print("Addition of two numbers :",Add)
    elif Choice==2:
        Sub=Num1-Num2
        print("Subtraction of two numbers:",Sub)
    elif Choice==3:
        Mux=Num1*Num2
        print("Multiplication of two numbers:",Mux)
    elif Choice==4:
        div=Num1/Num2
        print("Division of two numbers:",div)
    else:
        print("Invalid choice!")
except ZeroDivisionError:
    print("Zero value is not possible for b to division. please enter any other number!")
except ValueError:
    print("You have entered character! please enter any number!")
except Exception:
    print("Something went wrong!")