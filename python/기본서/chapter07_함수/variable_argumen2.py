# 가중치를 전달해서, 가중치의 곱의 합을 리턴
# 가변인수 사용할 것.
# 가변인수의 위치는 변수 중 마지막!
import math
def intsum(weight,*ints):
    total = 0
    for num in ints:
        total += num * weight
    return total

#print(intsum(0.1,1,1,2,3,4,5))
values = range(1,10)
#intsum(0.9,values)

# intsum 함수는 2개의 인자로 본다. 1개는 0.9, 1개는 ((1,2,3...10))
# 단일 튜플이 아닌, 이중 튜플로 보기에 제대로 동작 X
# 따라서 호출문에서 펼처라의 의미를 갖고있는 *를 사용해야함

print(round(float(intsum(0.1,*values)),3))

# round 함수는 0을 포함하지 않음. 0까지 포함하려면 format 사용
print(format(float(intsum(0.1,*values)),".2f"))

