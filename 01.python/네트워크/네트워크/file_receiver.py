from _thread import*
import socket


HOST = '127.0.0.1'
PORT = 6000
FILE_PATH = 'C:/Users/KMJ/Pictures/received/data.jpg'

def receive_thread(client_socket, addr):
    try:
        # 파일 크기 수신
        size = client_socket.recv(1024)
        size = int(size.decode())
        print('수신할 파일 크기:',size)

        # 준비 되었다고 송신
        client_socket.send('ready'.encode())

        # 파일 수신
        total_size = 0
        with open(FILE_PATH, 'wb') as f:
            while True:
                # receiver 쪽에서 512로 sender보다 작게 설정되더라도
                # (TCP) Stream 전송(흐름 전송)이므로 두개로 나눠서 받음.
                # 따라서 받을 수 있음.
                data = client_socket.recv(1024) 
                f.write(data)
                total_size += len(data)
                if total_size >= size: break

            print(f'수신 완료: {total_size} bytes')
    
    except Exception as e:
        print(e)
    finally:
        client_socket.close()

with socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            client_socket, addr = s.accept()
            start_new_thread(receive_thread, (client_socket, addr))

    except Exception as e:
        print(e)