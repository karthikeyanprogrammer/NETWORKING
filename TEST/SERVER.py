import socket
import threading
HEADER_LEN=64
SERVER_IP=socket.gethostbyname(socket.gethostname())
PORT=5050
FORMAT='utf-8'
ADDR=(SERVER_IP,PORT)
DISCONNECT_MSG='!*DISCONNECT*!'
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(client,client_addr):
    print(F'>> NEW CLIENT CONNECTED [{client_addr}]\n')
    print(f'>> ACTIVE CONNECTION [{threading.active_count()-1}] ...\n')
    connected=True
    while connected:
        msg_len=client.recv(HEADER_LEN).decode(FORMAT)
        if msg_len:
            msg_len=int(msg_len)
            msg=client.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected=False
                print(f'>> CLIENT DISCONNECTED [{client_addr}]\n')
                print(f'>> ACTIVE CONNECTION [{threading.active_count()-2}] ...\n')
            else: 
                print(f'>> MESSAGE FROM [{client_addr}] MESSAGE [{msg}]\n')
    client.close()
def start():
    server.listen()
    while True:
        client,client_addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(client,client_addr))
        thread.start()
print(F'>> STARTING SERVER AT PORT [{PORT}], IP [{SERVER_IP}] ...\n')
start()