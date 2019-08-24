import socket
from time import ctime

HOST = '192.168.1.103'
PORT = 8080
SENSOR_PORT_NO=7005
BUFSIZE = 1024
ADDR = (HOST, PORT)
CLIENT_ADDR=(HOST,SENSOR_PORT_NO)

#udpCliSock = socket(AF_INET, SOCK_DGRAM)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(CLIENT_ADDR)

while True:

    print("...waiting for response...")
    #recv_data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    recv_data, ADDR = client.recvfrom(1024)
    if recv_data is None:
        break
    else:
        #recv_data = recv_data.decode()
        #print("[%s]: receiving data from server %s:%s  :%s" % (ctime(), ADDR[0], ADDR[1], recv_data))
        sendData = recv_data
        client.sendto(sendData, ADDR)


client.close()