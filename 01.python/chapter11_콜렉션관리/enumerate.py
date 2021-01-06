# enumerate = 나열된
# 인덱스를 자동으로 생성해 줌. 
# 인덱스와 데이터는 튜플형식
# 사용빈도 높음
import random

# 예시 1
score = random.sample(range(70,100),5)
print(score)
for no, s in enumerate(score,1):
    print(str(no)+'번 학생의 성적:',s)
