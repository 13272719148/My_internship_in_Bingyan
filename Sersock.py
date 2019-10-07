'''   
这是创建UDP服务器的伪代码
ss = socket()                                            #创建服务器socket
ss.bind()                                                #绑定服务器socket 
inf_loop:                                                #服务器的无限循环
    cs = ss.recvfrom()/ss.sendto()                       #服务器的接收/发送 
ss.close()                                               #关闭服务器（不过好像一般用不到
'''
#-*- coding:unicode_escape -*-
from socket import *                                     #引入模块socket和time
from time import ctime      
def examine_ones(data_b):                                                               #定义奇偶检测函数
    examine_check = data_b[0]                                                           #取分组第一位为检验位
    examine_object = data_b[1:]                                                          #取分组第二位以后为检验消息位
    nums_of_ones = 0                                                                    #二进制中“1”个数计时器归零
    for i in examine_object:                                                            #对于消息里的每一个对象
        i_b = bin(i)                                                                    #将其转化为二进制字符串
        for bit,nums in enumerate(i_b):                                                 #对于二进制字符串中的每一位进行迭代
            if nums == "1":                                                             #如果该位为1
                nums_of_ones += 1                                                       #则计数器加1
    if nums_of_ones % 2 == 1 and examine_check == b"1"[0]:                              #如果检验位为1并且消息位的1的个数是奇数
        return True                                                                     #返回True
    elif nums_of_ones % 2 == 0 and examine_check == b"0"[0]:                            #如果检验位为0并且消息位的1的个数是偶数
        return True                                                                     #返回True
    else:                                                                               #其他情况均为错误
        return False                                                                    #返回False

def ack(data,addr,bool_situation_str_lower):                                            #定义发送ack函数（数据、地址、布尔情况
    data_tosend = chr(data[1]).encode("unicode_escape") + bool_situation_str_lower.encode("unicode_escape")           #拼接序号+布尔情况作为ack
    UDPSerSock.sendto(data_tosend,addr)                                                 #发送数据到addr
HOST = ''                                                #主机名取任何可用的（对bind的标识
PORT = 21569                                             #取一个可用端口
BUFSIZ = 50                                              #缓存区规定50字节
ADDR = (HOST, PORT)                                      #服务器地址

UDPSerSock = socket(AF_INET, SOCK_DGRAM)                 #创建服务器的套接字
UDPSerSock.bind(ADDR)                                    #讲地址绑定到套接字

while True:                                              #循环开始
    print('waiting for message...')                      
    data_rcvall = b""                                    #创建一个空的bytes变量来装载接收的数据
    data_buf = []                                        #创建列表以装载接收过的数据
    while True:                                          
        data, addr = UDPSerSock.recvfrom(BUFSIZ)         #接收分包数据
        if examine_ones(data):                           #如果通过奇偶检测
            ack(data,addr,"true")                        #发回序号+true
            data_str = data[1:].decode("unicode_escape")     #舍弃数据检验位并解码
            if data_str not in data_buf:                     #如果列表中不存在数据
                data_buf.append(data_str)                    #将数据添加到列表
        else:                                            #反之
            ack(data,addr,"false")                       #发回序号+false                                  
        if len(data) < BUFSIZ:                           #此时已完成最后一组的确认(条件控制有错)
            break                                        
    data_buf.sort()                                               #按照序号将数据列表排序 
    for i,j in enumerate(data_buf):                               #enmerate迭代接收数据的列表
        data_buf[i] = j[1:]                                       #将列表每一项都去除序号
    data_rcvall = ''.join(data_buf)                               #将列表中每一个对象都连接起来
    data_b_time = '[{}]'.format(ctime())                          #添加时间戳data_b_time
    data_b_final = data_b_time + data_rcvall                      #拼接时间戳和数据
    print(data_b_final)                                           #打印收到的时间戳消息     
    print('...received from and returned to:',addr)      #打印消息以提示
UDPSerSock.close()                                       #关闭UDP服务器








