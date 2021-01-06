# 내림차순
import random
# 1~100 범위에서 10개의 랜덤한 숫자로된 리스트 구성
random.seed(0)
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