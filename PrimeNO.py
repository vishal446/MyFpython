num=int(input("Enter a number:"))
i=2
while i<=num-1:
    if num%i==0:
        print(f"{num} is not prime")
        break;
    i=i+1
else:
    print(f"{num} is prime")


