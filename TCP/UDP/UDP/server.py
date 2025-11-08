import socket

UDP_IP="127.0.0.1" #listening on localhost
UDP_PORT= 5005 #port to listen on

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #create UDP socket
sock.bind((UDP_IP,UDP_PORT)) # bind socket to ip and port

print(f"listening for UDP packets on {UDP_IP}:{UDP_PORT}")

while True:
    data,addr =sock.recvfrom(1024) #buffer size is 1025 bytes (lower the number more the speed and more cpu consumption)
    print(f"received message from {addr}:{data.decode('utf-8')}")