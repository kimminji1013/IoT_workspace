# 파일 읽기
# f.read () --> 파일 전체 내용
# f.read (n) --> n 개의 내용, 주로 binary 파일
# f.readline () --> 한 줄
# f.readlines () --> 전체 라인 리스트
# 각 라인의 끝에 개행 문자(\n)가 들어 있음

# IO작업들은 예외 처리를 해주는 것이 권장사항임.


# read로 파일 읽기
"""
try:
    f = open("live.txt",'rt',encoding='utf-8')
    text = f.read(10)
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()
"""


#  readline으로 파일 읽기
"""
try:
    text = ""
    line = 1    
    with open("live.txt",'rt',encoding='utf-8') as f:
        while True:
            row = f.readline()
            if not row: break
            text += str(line) + ":" + row
            line += 1
        print(text)
except Exception as e:
    print("예외발생,",e)
"""

# readlines()이용해서 파일 읽기
f = open("live.txt",'rt',encoding='utf-8')
rows = f.readlines()
for no, s in enumerate(rows,1):
    print(f'{[no]} : {s}', end='') #readlines()자체에 개행문자 존재

f.close


