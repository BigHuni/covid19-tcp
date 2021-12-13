from socket import *
import threading
import asyncio
import os
import schedule, time
from search import CoronaDataStack as CDS

def filesend(sock):
    jpath = os.getcwd()
    filename = f'{jpath}/covid19.json'
    print(f"Sending '{filename}'")
    fn = filename.split('/')
    sock.sendall(fn[-1].encode())
    with open(filename, 'rb') as f:
        sock.sendfile(f, 0)

async def tcp():
    port = 8081
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind(('', port))
    serverSock.listen(1)
    print(f'{port}번 포트로 접속 대기중...')
    connectionSock, addr = serverSock.accept()
    print(str(addr), '에서 접속했습니다.')
    filesend(connectionSock,)
    serverSock.close()
    await asyncio.sleep(30)
    await tcp()

def tasksched():
    schedule.every().day.at('13:00').do(CDS)
    while True:
        schedule.run_pending()
        time.sleep(1)

async def main():
    TCD = threading.Thread(target=tasksched)
    TCD.start()
    await tcp()

asyncio.run(main())