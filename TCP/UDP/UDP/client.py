import socket

UDP_IP ="127.0.0.1" #target ip address (where the server is running)
UDP_PORT= 5005 # target port (where the server is listening)
MESSAGE ="hello, UDP!"

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #create udp socket
sock.sendto(MESSAGE.encode('utf-8'),(UDP_IP,UDP_PORT)) #send the message
print(f"sent message:{MESSAGE} to {UDP_IP}:{UDP_PORT}")
sock.close()