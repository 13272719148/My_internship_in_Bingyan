from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

UDPClientSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>>>')
    if not data:
        break
    UDPClientSock.sendto(data,ADDR)
    data, ADDR = UDPClientSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data)

UDPClientSock.close()