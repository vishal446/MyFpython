class Room:
    def get_room_dimension(self,l,b):
        self.l=l
        self.b=b

    def cal_area(self):
        area=self.l*self.b
        print("Area=",area)

class Kitchen_room(Room):       #kitchen_room inherit Room
    def msg(self):
        print("this is kitchen room")


k=Kitchen_room()
k.msg()
k.get_room_dimension(5,2)  # room or parent
k.cal_area()

'''
r=Room()
r.get_room_dimension(5,2)
r.cal_area()'''