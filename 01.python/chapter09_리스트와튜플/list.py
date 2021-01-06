# 리스트 = 자료의 집합
# 리스트에서 문자열은 불변객체 이기에 변경이 불가능하다.
# 문자열을 읽을 수만 있음. 쓰기 교체는 안됨
import random
"""
score = random.sample(range(80,100),5)
total = 0

for s in score:
    total += s

print("total:", total)
print("average:", total/len(score))

print(list("KOREA"))
"""

# list ex01
"""
nums = list(range(0,10))
print(nums[:])
print(nums[2:5])
print(nums[:4])
print(nums[6:])
print(nums[1:7:2])

score2 = random.sample(range(80,100),5)
print(score2[2])
score2[2] = 55
print(score2[2])
print(score2)
"""

# list ex02
# 더하기, 곱하기는 문자열이던 리스트이던 동일 sequence이기에 
# 처리는 같다. +는 이어 붙이기, *는 반복
