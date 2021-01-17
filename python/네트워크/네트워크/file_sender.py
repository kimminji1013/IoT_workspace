# client가 sender, server가 receiver
# 서버가 보내는 file size는 매번 다름. 파일은 1024byte로 쪼개서 보낼 것임.
# receiver가 받은 data 크기가 원본 파일과 같다면 다 받았다고 판단 할 것.

# with 명령어 :  with 가 끝나면 자동으로 close 해주는 명령어 
# ex) with open('file name')as f 로 사용했었음
# socket도 close 해줘야 하니까 with 사용할꺼임!

import os
import socket
HOST = '127.0.0.1'
PORT = 6000
FILE_PATH = 'C:/Users/KMJ/Pictures/prideandprejudicemovieclip.jpg'

def file_read(file_path):
    with open(file_path,'rb') as f: # 어떤 파일인지 모르니까 binary로 읽음
        while True: #generator
            data = f.read(1024)
            if not data:
                break
            yield data


with socket.socket() as s:
    try:
        s.connect((HOST, PORT))
        fileSize = os.path.getsize(FILE_PATH)

        # 파일 크기 전송
        print('전송 파일 크기', fileSize)
        s.sendall(str(fileSize).encode())

        # 준비 상태 수신
        isready = s.recv(1024).decode() # receiver로부터 받을 준비 되었다고 수신
        if isready == "ready": # 파일 전송하기
            for data in file_read(FILE_PATH):
                s.sendall(data)
            print("전송 완료")

    except Exception as e:
        print(e)

