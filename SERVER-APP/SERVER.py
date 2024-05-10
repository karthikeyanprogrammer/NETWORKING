import socket
import threading
import tkinter as tk
header_len=64
port=5050
server_ip=socket.gethostbyname(socket.gethostname())
server_addr=(server_ip,port)
format='utf-8'
disconnect_msg='!*DISCONNECT*!'
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(server_addr)
clients={}
def handle_client(client,client_addr):
    print(F'>> NEW CLIENT CONNECTED [{client_addr}]\n')
    print(f'>> ACTIVE CONNECTION [{threading.active_count()-1}] ...\n')

    connected=True
    clients[client]=client_addr
    while connected:
        msg=client.recv(header_len).decode(format)
        if msg:
            if msg==disconnect_msg:
                connected=False
            else:
                for c,ca in clients.items():
                    if ca!=client_addr:
                        client.send(msg)
                        print(f'>> MESSAGE FROM [{client_addr}] HAS BEEN DIDTRIBUTED TO CLIENTS\n')
    client.close()
    del clients[client]
    print(f'>> CLIENT DISCONNECTED [{client_addr}]\n')
    print(f'>> ACTIVE CONNECTION [{threading.active_count()-1}] ...\n')
def start():
    server.listen()

    while True:
        client,client_addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(client,client_addr))
        thread.start()

print(F'>> STARTING SERVER AT PORT [{port}], IP [{server_ip}] ...\n')
