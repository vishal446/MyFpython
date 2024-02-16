# making a pie chart

import matplotlib.pyplot as str
std=(["Raju", "Vijay", "Brijesh", "Pankaj", "Dinesh"])
Mark=([33,40,90,50,60])
str.axis("equal")
str.pie(Mark,labels=std,radius=1, explode=[0.1,0,0.15,0,0],autopct='%0.1f%%')
str.title("Pie chart of students percentage")
str.savefig("piechart.png")
str.show()