import matplotlib.pyplot as su
x=([100,34,56,89,90])
y=(['vishal','durgesh','pratap','brijesh','nitin'])
su.plot(x,y,color='red',linewidth='5',linestyle='dotted')
su.ylabel("student name")
su.xlabel("marks")
su.title("bachcho ke mehnat ka phal")
su.grid()
su.show()