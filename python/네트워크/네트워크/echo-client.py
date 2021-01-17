# 내가 접속 할 서버의 주소와 포트번호
# 1. 소켓을 만든다
# 2. 커넥트를 호출한다.
# 3. 해당 주소의 서버와 연결된다.
# 4. 메시지를 보낸다. send 보다는 sendall 사용, encode로 문자열 binary로 변경
# 5. 서버한테 또 메시지가 돌아오니까. recv로 수신. 
#   - 역시나 binary이므로 decode해서 출력.

import socket

HOST = '127.0.0.1'
PORT = 9999
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버와 연결
client_socket.connect((HOST, PORT))
# 메시지 전송
client_socket.sendall('Hello'.encode())
# 메시지 수신
data = client_socket.recv(1024)
print('Received', data.decode())

client_socket.close()