# 실행할 명령이 보장을 못하겠을 때, 
# try:
# 실행할 명령
# except 예외 as 변수:
# 어떻게 대처할지 처리 
# else: #옵션임
# 예외 발생하지 않을 때 처리

str = '89ㄴㅇㄹ'
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError:
    print('점수의 형식이 잘못되었습니다.')
except IndexError:
    print('첨자 범위를 벗어났습니다.')

print('작업완료')
