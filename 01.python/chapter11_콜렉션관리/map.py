# map 함수
# map 함수 결과 값은 list 아니라서 list 모듈 사용해주는게 좋음
# 매개변수 자리에 함수를 넣어 사용하는 fuctional programming 이라 한다.


import random
"""
def total(s,b):
    return s+b

score = random.sample(range(40,91),5)
bonus = random.sample(range(1,10),5)

for s in map (total,score,bonus):
    print(s,end=',')
"""

# 문자열 리스트 정수 리스트로 바꾸기
score = ['10','20','30','40','50']
print(score)

# enumerate 사용
"""
for i,s in enumerate(score):
    score[i] = int(s)
print(score)
"""
# enumerate 사용X

for idx in range (len(score)):
    score[idx] = int(score[idx])

print(score)