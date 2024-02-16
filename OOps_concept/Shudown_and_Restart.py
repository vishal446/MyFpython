import os
print('1.Press 1 Shutdown, \n 2.Press 2 for Restart,\n 3.Press 3 for exit\n')
choice=int(input("Enter above number:"))
if choice>=1 and choice<=2:
    if choice==1:
        os.system("shutdown /s /t 1")
    else:
        os.system('shutdown /r /t 1')
else:
    exit()