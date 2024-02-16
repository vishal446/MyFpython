Year=int(input("Enter a Year:"))

if Year%100==0:
    if Year%400==0:
        print("Leap Year")
    else:
        print("Ordinay Year")
elif Year%4==0:
    print("Leap Year!")
else:
    print("Ordinay Year")
