import socket
import time
HEADER_LEN=64
PORT=5050
FORMAT='utf=8'
DISCONNECT_MSG='!*DISCONNECT*!'
SERVER_IP='192.168.0.5'
SERVER_ADDR=(SERVER_IP,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(SERVER_ADDR)

def send(msg):
    msg=msg.encode(FORMAT)
    msg_len=len(msg)
    send_len=str(msg_len).encode(FORMAT)
    send_len+=b' '*(HEADER_LEN-len(send_len))
    client.send(send_len)
    client.send(msg)
connected=True
while connected:
    msg=input('>> ')
    if msg==DISCONNECT_MSG:
        send(DISCONNECT_MSG)
        connected=False
    send(msg)
