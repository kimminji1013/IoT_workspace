# 가변 인수
# 인수의 수가 고정되어 있지 않음 ex) print()
# 함수에서는 이를 tuple 변수로 받음
"""
def intsum(*ints):
    total = 0
    for num in ints:
        total += num
    return total

print(intsum(1,2,3))
"""
# 오류(음수)가 있는 경우
"""
def intsum(*ints):
    total = 0
    for num in ints:
        if num>0:
            total += num
        else:
            continue
    return total

print("잘못된 데이터를 제거 후 계산했습니다.\
    \ntotal =",intsum(8,9,6,2,-9,7,5,8))
"""
# None 이용하기
def intsum(*ints):
    total = 0
    for num in ints:
        if num<0:
            return 0
        total += num
    return total

total = intsum(8,9,6,2,-9,7,5,8)
if total:
    print('total = ',total)
else:
    print('잘못된 데이터를 제거 후 계산했습니다.')