# Python이 제공해주는 module을 표준 module 이라고 부른다.
# ex) random, time ...


import time
t = time.time()
#print(t)
#print(time.ctime(t))

t = time.localtime(t) #지금 이 명령어를 수행하는 컴퓨터 기준.
print(t)
print(f'{t.tm_year}--{t.tm_mon}--{t.tm_mday}')