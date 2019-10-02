'''
clisocket = socket()                        #创建客户端的socket
comm_loop:                                  #通信的循环
    clisocket.sendto()/clisocket.recvfrom() #对话：发送和接收
clisocket.close()                           #关闭客户端socket
'''




from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

UDPClientSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>>>')
    data_b = data.encode("UTF-8")
    if not data_b:
        break
    UDPClientSock.sendto(data_b,ADDR)
    data_b, ADDR = UDPClientSock.recvfrom(BUFSIZ)
    data_b = data_b.decode("UTF-8")
    if not data_b:
        break
    print(data_b)

UDPClientSock.close()