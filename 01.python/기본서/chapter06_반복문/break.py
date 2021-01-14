# 반복문을 벗어나고 싶을 때
import random

score = random.sample(range(60,100),5)
#score = random.shuffle(score)

for s in score:
    if (s<0) or (s>100):
        break
    print(s)

print('성적 처리 끝')
