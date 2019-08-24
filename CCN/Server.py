import socket
from time import ctime

HOST = '192.168.1.103'
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
    print("...waiting for message...")
    data, ADDR = udpSerSock.recvfrom(BUFSIZE)
    orgdata=data.decode()
    print(orgdata)
    if data is None:
        break
    print("[%s]: From Address %s:%s receive data: %s" % (ctime(), ADDR[0], ADDR[1], orgdata))

    #send_data = input("> ")
    #if send_data is not None:
    #    udpSerSock.sendto(send_data.encode(), ADDR)
udpSerSock.close()