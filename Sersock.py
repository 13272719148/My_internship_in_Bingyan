'''   
这是创建UDP服务器的伪代码
ss = socket()                                            #创建服务器socket
ss.bind()                                                #绑定服务器socket 
inf_loop:                                                #服务器的无限循环
    cs = ss.recvfrom()/ss.sendto()                       #服务器的接收/发送 
ss.close()                                               #关闭服务器（不过好像一般用不到
'''
from socket import *                                     #引入模块socket和time
from time import ctime      

HOST = ''                                                #主机名取任何可用的（对bind的标识
PORT = 21567                                             #取一个可用端口
BUFSIZ = 1024                                            #缓存区规定1KB
ADDR = (HOST, PORT)                                      #服务器地址

UDPSerSock = socket(AF_INET, SOCK_DGRAM)                 #创建服务器的套接字
UDPSerSock.bind(ADDR)                                    #讲地址绑定到套接字

while True:                                              #循环开始
    print('waiting for message...')                      
    data, addr = UDPSerSock.recvfrom(BUFSIZ)             #获取客户端消息和地址
    data_str = data.decode("UTF-8")                      #解码消息
    data_b_time = '[{}]'.format(ctime())                 #添加时间戳data_b_time
    data_b_tosend = data_b_time + data_str               #拼接字符串
    data_b_tosend = data_b_tosend.encode("UTF-8")        #编码UTF-8字符串
    UDPSerSock.sendto(data_b_tosend,addr)                #向客户端地址发送UTF-8编码
    print('...received from and returned to:',addr)      #打印消息以提示
UDPSerSock.close()                                       #关闭UDP服务器