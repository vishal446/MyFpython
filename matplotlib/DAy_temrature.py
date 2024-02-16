# Write a program to make a graph

import matplotlib.pyplot as da

Day=(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
Max_tem=([28,29,30,33,36,40,45])
Min_tem=([25,28,20,31,30,35,39])
# da.plot(Day,Tem,'r+--')
# da.plot(Day,Tem,color='green',marker='D',markersize='20')
da.plot(Day,Max_tem,color='green',label='Max')
da.plot(Day,Min_tem,'r',label='Min')
da.legend(loc="best",shadow='20',fontsize="large")
da.xlabel("Days")
da.ylabel("Temprature")
da.grid()
da.title("WEATHER iNFORMATION")
da.savefig("Weatherinfo.png")
da.show()
