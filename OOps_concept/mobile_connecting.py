import socket

ob=socket.socket()
ob.bind(('192.168.43.182',2302))
ob.listen(4)
clientobject,add=ob.accept()
conn=True
while conn:
    gotmsg=clientobject.recv(1024)
    gotmsg.decode('utf-8')
    print(gotmsg)
    if len(gotmsg)==0:
        conn=False
        ob.close()
# ob.close()