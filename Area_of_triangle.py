try:
    _a_side=int(input("Enter value of side a:"))
    _b_side=int(input("Enter value of side b:"))
    _c_side=int(input("Enter value of side c:"))
    _Semi_parimeter=(_a_side+_b_side+_c_side)/2
    _Area_of_Triangle=(_Semi_parimeter*(_Semi_parimeter-_a_side)*(_Semi_parimeter-_b_side)*(_Semi_parimeter-_c_side))**0.5
    print("Area of Triangle is :",_Area_of_Triangle)
except ValueError:
    print("You have entered character please enter any number!")
except Exception:
    print("something wrong")