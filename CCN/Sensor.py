import socket
from time import ctime

CLIENT_IP = '192.168.1.103'
PORT = 7005
BUFSIZE = 1024
ADDR = (CLIENT_IP, PORT)
udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sendData = input("> ")
    if sendData is None:
        break
    else:
        udpCliSock.sendto(sendData.encode(), ADDR)

    #print("...waiting for response...")
    #recv_data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    #if recv_data is not None:
    #    print("[%s]: receiving data from server %s:%s  :%s" % (ctime(), ADDR[0], ADDR[1], recv_data.decode()))