import socket
import datetime
s=('',)
msg=''
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ('127.0.0.1' , 5006)

def recv():
    data, addr = sock.recvfrom(1024)
    orgdata = data.decode('utf-8')
    print('Reply : ', orgdata)
    print('Address , Port : ', addr)
    now = datetime.datetime.now()
    print('Timestamp: ', now.strftime("%Y-%m-%d %H:%M:%S"))

def send(msg,addr):
    sock.sendto(msg,addr)

while s[0]!='stop' or msg!='stop':
    msg=input('Enter your message:')
    if(msg == 'stop'):
        print('Connection Terminated')
        break
    else:
        byt=msg.encode('utf-8')
        send(byt,address)
        recv()
