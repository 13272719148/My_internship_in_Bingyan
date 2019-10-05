'''
clisocket = socket()                        #创建客户端的socket
comm_loop:                                  #通信的循环
    clisocket.sendto()/clisocket.recvfrom() #对话：发送和接收
clisocket.close()                           #关闭客户端socket
'''




from socket import *                                      #import socket的everything

HOST = 'localhost'                                        #主机名（ip
PORT = 21567                                              #端口
BUFSIZ = 4                                                #设置缓冲区大小4字节
ADDR = (HOST,PORT)                                        #地址设定

UDPClientSock = socket(AF_INET, SOCK_DGRAM)               #创建AF_INET族的SOCK_DGRAM的套接字

while True:                                               #发送消息循环
    data = input('>>>')                                   #获取输入信息
    data_b = data.encode("UTF-8")                         #转换信息为UTF-8码
    if not data:                                          #若输入信息为空则停止
        break
    UDPClientSock.sendto(data_b,ADDR)                     #向ADDR地址（服务器）发送data_b数据报
    data_b, ADDR = UDPClientSock.recvfrom(BUFSIZ)         #接收信息和地址（ADDR貌似没用了
    data_b = data_b.decode("UTF-8")                       #对data_解码
    if not data_b:                                        #若接收的消息为空则停止
        break
    print(data_b)                                         #打印data_b内容

UDPClientSock.close()                                     #关闭客户端socket