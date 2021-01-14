# list comprehension(이해)
import random
# ex01
"""
nums = [n*2 for n in range(1,11) if n%2==0]
for i in nums:
    print(i, end=', ')
"""

"""
nums = []
for n in range(1,11):
    nums.append(n*2)

print(nums)

print([n for n in range(1,11) if n%3==0])
"""

# ex02

random_nums = [random.randrange(1,101) for i in range(50)]
print(random_nums)

# 이렇게 코드에서 사용되지 않는 변수가 생길 때 (i)
# 보통 변수명을 _로 정하는 관례가 있다.  