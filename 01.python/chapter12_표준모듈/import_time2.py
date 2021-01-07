import time

# 0~999 출력 시간
# 컴퓨터에서 입출력(IO) 작업은 시간이 좀 걸림. >>>0.38초 
"""
start = time.time()
for a in range(1000):
    print(a)
end = time.time()

print(end-start)
"""

#>>> 0.0 (측정 불가) -> 1000번 계산은 너무 빨라 측정 불가임.
"""
start = time.time()
total=0
for a in range(1000):
    total+=a
end = time.time()
print(end-start)
"""

# 실행 멈춤
# sleep 명령어
"""
print('Hello~')
time.sleep(1)
print('If there are two man who\'s name is 성시경 at night,\
 what do we call about this situation? ')
time.sleep(5)
print('야간투시경')
"""

# strftime 함수
# 문자열 포멧팅 시간으로 직독직해 할 수 있음
# time 정보를 문자열로 포멧팅 하겠다는 뜻.
import datetime
timestr = time.strftime('%Y-%m-%d', time.localtime())
timestr2 = time.strftime('%H:%M:%S', time.localtime())
print(timestr,'\n',timestr2)

# Y : 4자리 연도
# y : 2자리 연도
# m : 월
# d : 일
# H : 시간(24시간)
# I : 시간(12시간)
# M : 분
# S : 초
