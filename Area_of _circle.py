try:
    _rad=float(input("Enter radius of circle:"))
    _Area=3.14*_rad**2
    print("Area of Circle:",_Area)
except ValueError:
    print("You have entered character! please enter any number!")
except Exception:
    print("Something went wrong!")