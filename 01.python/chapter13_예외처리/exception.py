# 에러의 종류에 상관 없이 예외 발생시 모두 실행
# 기존에는 FileNotFoundError 처럼 특정 상황 지정해줬는데,
# 이거 쓰면 try의 파일 없는 경우 외 다른 경우에서 에러가 발생했을 때에도
# 포괄적으로 사용



f = None
try:
    f = open("../chapter14_파일/live.txt",'rt',encoding='utf-8')
    text = f.read(10)
    print(text)
except Exception as e:
    print("예외발생,",e)
finally:
    if f: # 파일이 열려서 f값이 True 일 경우에
        f.close()


# 방법 2
# try:
#     with open("C:\Users\KMJ\IoT_workspace\01.python\chapter14_파일live.txt",\
#         'rt',encoding='utf-8') as f
#     text = f.read(10)
#     print(text)
# except Exception as e:
#     print("예외발생,",e)
