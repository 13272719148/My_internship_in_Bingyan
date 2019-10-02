'''   
这是创建UDP服务器的伪代码
ss = socket()                           #创建服务器socket
ss.bind()                               #绑定服务器socket 
inf_loop:                               #服务器的无限循环
    cs = ss.recvfrom()/ss.sendto()      #服务器的接收/发送 
ss.close()                              #关闭服务器（不过好像一般用不到
'''
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

UDPSerSock = socket(AF_INET, SOCK_DGRAM)
UDPSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = UDPSerSock.recvfrom(BUFSIZ)
    data_str = data.decode("UTF-8")
    data_b_time = '[{}]'.format(ctime())
    data_b_tosend = data_b_time + data_str
    data_b_tosend = data_b_tosend.encode("UTF-8")
    UDPSerSock.sendto(data_b_tosend,addr)
    print('...received from and returned to:',addr)
UDPSerSock.close()