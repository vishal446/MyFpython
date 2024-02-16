try:
    Num = int(input("Enter a number:"))
    rem=0
    Num1 = 0
    Num2=Num
    while Num != 0:
        rem = Num % 10
        Num1 = Num1 + (rem * rem * rem)
        Num = Num // 10
    if Num1 == Num2:
        print(f"{Num2} is amstrong number")
    else:
        print(f"{Num2} is not amstrong number")
except ValueError:
    print("You entered character! please enter any number!")
except Exception:
    print("Something went wrong!")