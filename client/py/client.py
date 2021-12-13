from socket import *
import threading
import time
import os

######c로 짤 때 필요없는 부분(저장되는 파일위치 설정하는 코드)
path = os.path.dirname( os.path.abspath( __file__ ) )+"/config.env"
p = open(path,"r",encoding="utf-8")
pstr = p.read().split()[0]
print(pstr)
######

ip = input("ip_address\n>> ")
port = int(input("port num\n>> "))

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip, port))

print('connected')


fn = clientSock.recv(1024).decode()

with open(pstr + fn, 'wb') as f:
    print('file opened')
    print('receiving file...')
    data = clientSock.recv(8192)
    f.write(data)

print('Download complete')
clientSock.close()
print('task finished')