'''
from socket import *
ss = socket()
ss.bind()
inf_loop:
    cs = ss.recvfrom()/ss.sendto()
ss.close()
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
    UDPSerSock.sendto('[%s]%s'%(ctime(),data),addr)
    print('...received from and returned to:',addr)
UDPSerSock.close()