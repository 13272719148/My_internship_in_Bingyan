'''
clisocket = socket()                        #创建客户端的socket
comm_loop:                                  #通信的循环
    clisocket.sendto()/clisocket.recvfrom() #对话：发送和接收
clisocket.close()                           #关闭客户端socket
'''


#-*- coding:unicode_escape -*-

from socket import *                                      #import socket的everything

HOST = 'localhost'                                        #主机名（ip
PORT = 21568                                              #端口
BUFSIZ = 4                                                #设置缓冲区大小4字节
ADDR = (HOST,PORT)                                        #地址设定
N = 4                                                     #设定GBN中未确认分组数N的大小
                                            

UDPClientSock = socket(AF_INET, SOCK_DGRAM)               #创建AF_INET族的SOCK_DGRAM的套接字

while True:                                               #发送消息循环
    data = input('>>>')                                   #获取输入信息
    data_b = data.encode("unicode_escape")                         #转换信息为unicode码
    if not data:                                                   #若输入信息为空则停止
        break
    for i in range(len(data_b)//4+1):                                     #将数据拆分成为长度小于等于4（buffersize）的包，分开发送
        if 4*(i+1) < len(data_b):                                         #对于前面的分组：
            numbers_of_one = 0                                            #分组中二进制1的数量计数器归零
            for find_one_numbers in data_b[4*i:4*i+4]:                    #对于分组中的每个元素：
                find_one_numbers_b = bin(find_one_numbers,2)              #将每个可迭代元素（unicode码）转化为二进制字符串
                for bit,numbers in enumerate(find_one_numbers_b):         #对于每一个二进制字符串：
                    if numbers == "1":                                    #如果有一位等于1
                        numbers_of_one += 1                               #计数器就加1
            if numbers_of_one % 2 == 1:                                    #如果计数器值为奇数
                data_tosend = "1".encode("unicode_escape") + data_b[4*i:4*i+4]      #在数据头部加上字符串1的二进制unicode码
            else:                                                                   #反之
                data_tosend = "0".encode("unicode_escape") + data_b[4*i:4*i+4]      #数据头部加的为0
            UDPClientSock.sendto(data_tosend,ADDR)                                  #发送数据报到服务器address
        else:                                                             #对于最后一个分组：
            numbers_of_one = 0                                            #操作同前，故省略
            for find_one_numbers in data_b[4*i:]:
                find_one_numbers_b = bin(find_one_numbers)
                for bit,numbers in enumerate(find_one_numbers_b):
                    if numbers == "1":
                        numbers_of_one += 1
            if numbers_of_one % 2 == 1:
                    data_tosend = "1".encode("unicode_escape") + data_b[4*i:]
            else:
                    data_tosend = "0".encode("unicode_escape") + data_b[4*i:]
            UDPClientSock.sendto(data_tosend,ADDR)


    data_b_rcvall = b"" 
    while True:                                                           #创建了receive_all变量以完全接收消息（大于缓存的）
        data_b_rcv, ADDR = UDPClientSock.recvfrom(BUFSIZ)                 #分包接收信息和地址（ADDR貌似在这里没用了）再组合
        data_b_rcvall +=  data_b_rcv                               
        if len(data_b_rcv) < BUFSIZ:
            break
    data_b_rcvall = data_b_rcvall.decode("unicode_escape")                         #对data_b解码
    print(data_b_rcvall)                                                  #打印data_b内容

UDPClientSock.close()                                                     #关闭客户端socket