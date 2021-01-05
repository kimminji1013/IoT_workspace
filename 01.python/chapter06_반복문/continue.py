# continue 이후 명령을 실행하지 않고, 다음 변수로 넘어감
import random

error = 0
score = random.sample(range(50,120),5)

for s in score:
    if s <0 or s>100:
         error += 1
         continue
    print(s)
print('error의 개수 : ', error)

# block단위 들여쓰기 Tab(->) shift(<-)