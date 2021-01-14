# 리스트는 [], 튜플은 ()
# 튜플은 추가/ 수정/ 삭제 불가
# 읽기만 가능하다. -> 리스트보다 속도가 빠르다.
# ()괄호 없이 ,로 나열된 것도 튜플이다.
import random
import time

#튜플 기본 예제
#score = (random.randrange(70,101) for _ in range(5))
"""
score = (random.sample(range(60,100),5))
total = 0

for s in score:
    total += s

print('total :',total)
print('average :', total/len(score))
"""

#튜플이라서 가능한 것 unpacking 기능!
"""
names = "이순신", "김유신", "강감찬"
lee, kim, kang = names #unpack
print(lee)
print(kim)
print(kang)
"""

# 튜플이라서 가능한 것2 swap!
"""
a,b = 3,7
print(a,b)
a,b = b,a
print(a,b)
"""

# 튜플이라서 가능한 것3 !
def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

#result = gettime()
#print(f'지금은 {result[0]}시 {result[1]}분 입니다.')
hour, minute = gettime()
print(f'지금은 {hour}시 {minute}분 입니다.')