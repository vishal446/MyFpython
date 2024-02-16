try:
    print("Enter Obtain marks in all subjects!")
    Hindi = int(input("Hind:"))
    English = int(input("English:"))
    Math = int(input("Math:"))
    Physics = int(input("Physics:"))
    Chemistry = int(input("Chemistry:"))
    Art = int(input("Art:"))
    Total_marks = int(input("Enter total marks :"))
    Total_Obtain_marks = Hindi + English + Math + Physics + Chemistry + Art
    Obtain_Percnetage = (Total_Obtain_marks * 100) / Total_marks
    print("Obtain percentage:", Obtain_Percnetage)
    if (Obtain_Percnetage>100):
        print("Something is wrong please recheck your marks!")
    elif (Obtain_Percnetage <= 100) and (Obtain_Percnetage >= 75):
        print("First Division pass !")
    elif (Obtain_Percnetage < 75) and (Obtain_Percnetage >= 45):
        print("Second Division pass !")
    elif (Obtain_Percnetage < 45) and (Obtain_Percnetage >= 33):
        print("Third Division pass !")
    else:
        print("Fail!")
except ValueError:
    print("You have entered character! please enter any number!")
except Exception:
    print("Something went wrong!")