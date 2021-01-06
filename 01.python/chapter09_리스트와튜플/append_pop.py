# 삽입, 연결, 삭제, 검색, 정렬
# append와 pop은 stack의 LIFO을 만족하는 명령어!

import random

# 삽입
# .append(값) : 리스트의 끝에 값을 추가
# .insert(위치, 값) : 지정한 위치에 값을 삽입
"""
nums = list(range(0,4))
print(nums)

nums.append(4)
print(nums)

nums.insert(0,99)
print(nums)
"""

# insert slicing  
# [2:2] = nums[2] 앞에 삽입됨.
"""
nums = list(range(1,5))
nums[2:2] = list(range(7,10))
print(nums)
"""

# 연결
"""
list1 = list(range(1,4))
list2 = list(range(4,8))
list1.extend(list2)
list3 = list1+list2
print(list3)
"""


# 삭제
"""
score = list(random.sample(range(60,100),8))
print(score)
score.remove(100)
"""

# .pop() : 리스트의 끝 요소를 삭제하고, 삭제한 요소 리턴
# 삭제한 요소를 리턴해 줌. 뭘 삭제했는지 알 수 있음
"""
score = list(random.sample(range(60,100),8))
print(score)
print(score.pop())
print(score.pop())
print(score.pop(1))
print(score)
"""

# 1~100 범위에서 10개의 랜덤한 숫자로된 리스트 구성
#random.seed(0)
"""
numbers = [random.randrange(0,101) for _ in range(10)]
print(numbers)

# 두 개의 요소를 서로 바꿔주는 함수
def swap(ix1, ix2):
    temp = numbers[ix1]
    numbers[ix1] = numbers[ix2]
    numbers[ix2] = temp

# 최대값을 찾아서, 0번과 바꾸세요.
for i in range(0, len(numbers)):
    max_value = max(numbers[i:])
    max_value_ix = numbers.index(max_value)
    swap(i,max_value_ix)
    
print(numbers)
"""


# 검색
# 값 in sequence, 값 not in sequence -> True/False로 반환
"""
ans = input('결제 하시겠습니까?')

if ans in ['yes','y','ok','예']:
    print('결제를 진행합니다.')
else:
    print('결제를 취소합니다.')
"""

# 정렬
"""
score3 = [random.randrange(80,101) for _ in range(5)]
print(score3)

score3.sort()
print(score3)

score3.reverse()
print(score3)
"""

# 정렬2
"""
country = ['Koera','japen','China','America']
country.sort()
print(country)

country.sort(key = str.lower)
print(country)
"""

# 정렬3
score3 = [random.randrange(80,101) for _ in range(5)]
print(score3)

sorted_score3 = sorted(score3, reverse = True)
print(sorted_score3)
