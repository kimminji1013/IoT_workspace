# filter 함수
# filter(판정함수, 시퀀스) -> 시퀀스
# 판정함수에서 TRUE값만 리턴
import random

#def flunk(s):
#    return s < 60

score = random.sample(range(30,100),5)
print(score)
for s in filter(lambda s:s<60, score):
# for s in filter(flunk, score):
    print(s, end=' ')


# comprehension 이용해보기
score2 = [ n for n in score if n<60]
print('\n')
print(score2)

