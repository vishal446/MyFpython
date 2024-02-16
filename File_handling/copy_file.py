f=open("vishu.txt",'r')
d=open("mani.txt",'w')
for data in f:
    d.write(data)
print(d)