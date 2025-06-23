import socket
import threading

s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect(('0.0.0.0',1555))
message=s.recv(1024)
print(message.decode())

    
def send():
    while(True):
        print("enter message:")
        message=input()
        s.send(message.encode())
    
def recv():
    while(True):
        message=s.recv(1024)
        print(message.decode())     


    
threading.Thread(target=send).start()   
threading.Thread(target=recv).start()   
