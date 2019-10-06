'''
clisocket = socket()                        #创建客户端的socket
comm_loop:                                  #通信的循环
    clisocket.sendto()/clisocket.recvfrom() #对话：发送和接收
clisocket.close()                           #关闭客户端socket
'''


#-*- coding:unicode_escape -*-

from socket import *                                      #import socket的everything
import time

HOST = 'localhost'                                        #主机名（ip
PORT = 21568                                              #端口
BUFSIZ = 50                                               #设置缓冲区大小50字节
bytes_tosend = BUFSIZ - 2                                 #每次可以发送的字节数为缓冲大小-2（一位用于奇偶校验，另外的一位用于加序号）
ADDR = (HOST,PORT)                                        #地址设定
N = 4                                                     #设定GBN中未确认分组数N的大小
                                            

UDPClientSock = socket(AF_INET, SOCK_DGRAM)               #创建AF_INET族的SOCK_DGRAM的套接字

while True:                                               #发送消息循环
    data = input('>>>')                                   #获取输入信息
    data_b = data.encode("unicode_escape")                         #转换信息为unicode码
    if not data:                                                   #若输入信息为空则停止
        break
    for i in range(len(data_b)//bytes_tosend+1):                                                #将数据拆分成为长度小于等于BUFSIZ（buffersize）的包，分开发送
        if bytes_tosend*(i+1) < len(data_b):                                                    #对于前面的分组：
            data_tosend = str(i).encode("unicode_escape") + data_b[bytes_tosend*i:bytes_tosend*i+4]   #为要发送的数据封装序列号
            add_check_and_send(data_tosend,check(data_tosend),ADDR)                                   #加上奇偶检测位并发送数据
        else:                                                             #对于最后一个分组：
            data_tosend = str(i).encode("encode_escape") + data_b[bytes_tosend * i:]
            add_check_and_send(data_tosend,check(data_tosend),ADDR)

        time_cost = 60.0
        ack_rev = []
        '''
        if (i-3) % 4 == 0 or i == range(len(data_b))//4:
            time_start = time.time()
            while time_cost > time.time() - time_start:
                data,ADDR = UDPClientSock.recvfrom(BUFSIZ)
                ack_rev.append(data[3])
                ack_rev.sort()                                            #每四组消息发送后等待ack/超时，但由于多线程技术学习困难暂未实现
        '''

UDPClientSock.close()                                                     #关闭客户端socket



def check(data_b):                                                        #定义奇偶检测函数                                                                                                         
    nums_of_ones = 0                                                      #设置二进制数据中“1”的计数器                                                                          
    for i in data_b:                                                      #对于数据中的每一个对象      
        i_b = bin(i)                                                      #用新变量将其转化为二进制来处理
        for bit,nums in enumerate(i_b):                                   #对i_b进行enumerate迭代
            if nums == "1":                                               #如果某一位的数字为1
                nums_of_ones += 1                                         #计数器加1
    if nums_of_ones % 2 == 1:                                             #如果计数器为奇数
        return True                                                       #返回True
    else:                                                                 #反之
        return False                                                      #返回False


def add_check_and_send(data,bool_situation,addr):                         #定义增加奇偶检测位及发送函数
    if bool_situation == True:                                            #假如布尔参数为True
        data = "1".encode("unicode_escape") + data                        #在数据头封装“1”
        UDPClientSock.sendto(data,addr)                                   #发送数据
        return                                                            #结束函数
    else:                                                                 #反之
        data = "0".encode("unicode_escape") + data                        #在数据头封装“0”
        UDPClientSock.sendto(data,addr)                                   #发送数据
        return                                                            #结束函数




