# 소켓이란,  socket 은 IP address 와 Port 넘버가 합쳐진, 
# 네트워크 상에서 서버 프로그램과 클리어언트 프로그램이 통신을 할 수 있도록 해주는 소프트웨어 장치이다.



import socket

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
# IPv4, TCP는 default 값이라서 그냥
# server_socket = socket.socket() 해도 됨.

# 포트 충돌시 재사용 옵션 설정. 
#server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT)) #튜플
server_socket.listen()

# accept 함수에서 대기, 클라이언트 접속 시 새로운 소켓 리턴
client_socket, addr = server_socket.accept()

print('Connected by', addr)

while True:
    # 메세지 수신 대기
    data  = client_socket.recv(1024) # 1024byte 크기
    if not data: # client가 close가 되면 빈칸 return됨. 그래서 break
        break
    
    # data.decode()-> byte array를 문자열로 변환해주는 것
    print('Received from', addr, data.decode())

    # 받은 문자열 다시 클라이언트로 전송(에코)
    client_socket.sendall(data)



client_socket.close()
server_socket.close()

