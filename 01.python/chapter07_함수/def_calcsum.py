#합 구하는 계산 함수 예제
"""
def calcsum(n):
    total = 0
    for n in range(n+1):
        total += n
    return total

print("~5 = ", calcsum(5))
"""

#합 구하는 계산 함수 예제 (인수 추가)
def calcsum(begin,end,add):
    total = 0
    for n in range(begin,end+1,add):
        total += n
    return total

print("sum = ", calcsum(1,10,5))