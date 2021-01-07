# 람다 함수
# 한 줄로 정의되는 함수의 축약 표현
# 함수의 이름이 없고, 변수에 대입해서 사용한다.
# lambda a:a+1 (인수:식)
import random

# ex1
"""
score = random.sample(range(40,91),5)
for s in map(lambda x:x/2,score):
    print(s, end=',')
"""

# 60점 이하의 성적이 포함되었는지 판단 = 과락 여부 판단하시오.
score = random.sample(range(40,91),5)
print(score)

result = list(map(lambda x: x<60,score))
print(any(result)) # list에 한 개라도 True가 있는가? 있다면 ture 리턴



