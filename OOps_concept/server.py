import socket

ob=socket.socket()
ob.bind(('localhost',2301))
ob.listen(4)
clientobject,add=ob.accept()
print("server is ready to accept connection")
print('connected with this address',add)
#receive data from client
'''gotmsg=clientobject.recv(1024)
gotmsg.decode('utf-8')
print(gotmsg)'''
conn=True
while conn:
    gotmsg=clientobject.recv(1024)
    gotmsg.decode('utf-8')
    print(gotmsg)
    if len(gotmsg)==0:
        conn=False
        ob.close()

# ob.close()
