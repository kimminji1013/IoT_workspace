import socket
from _thread import * 
# threading 보다 하위레벨에서 지원하는 모듈인 _thread

def threaded(client_socket, addr):
    print('Connected by :',addr[0], ':', addr[1])
    while True:
        try:
            # 데이터가 수신되면 클라이언트에 전송(에코과정)
            data = client_socket.recv(1024)
            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break
            print('Received from '+ addr[0], ':', addr[1], data.decode())
            client_socket.send(data)

        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0], ':', addr[1])
            break
    
    client_socket.close()

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()

print('server start')

while True:
    print('wait')
    client_socket, addr = server_socket.accept()
    # start_new_thread에 thread.start() 내장
    start_new_thread(threaded,(client_socket,addr))

server_socket.close()