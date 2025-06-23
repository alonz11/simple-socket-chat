import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0',1555))
s.listen()
print("waiting for clients to connect")

client,address=s.accept()
print("your connected to: ",address)
client.send("you are connected".encode())   
sMessage=client.recv(1024)
print(sMessage.decode())
    
def send():
    while(True):
        print("enter message:")
        message=input()
        client.send(message.encode())
    
def recv():
    while(True):
        
        message=client.recv(1024)
        print(message.decode())
        
threading.Thread(target=send).start()   
threading.Thread(target=recv).start()   
