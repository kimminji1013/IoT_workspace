"""student = 1
while student <= 5:
    print(student, "번 학생의 성적을 처리합니다.")
    student += 1"""

# 1~100 숫자 합
"""num = 1
total = 0
while num <= 100:
    total += num
    num += 1
print("total =", total)"""

# 1~100까지 짝수의 합, 홀수의 합 구하기
"""num = 1
num2 = 2
total = 0
total_2 = 0
while num <= 100:
    total += num
    total_2 += num2
    num += 2
    num2 += 2
print("total_odd =", total, "\ntotal_even =", total_2)"""

#version2
"""num = 1
total_odd = 0
total_even = 0

while num <= 100:
    if num%2 == 0:
        total_even += num
    else:
        total_odd += num
    num += 1

print("total_odd =", total_odd, "\ntotal_even =", total_even)"""

# 무한 루프
# while true:
#   print("무한 루프 입니다.")

while True:                 # true 소문자는 X
    print("enter\n")
    a = input('입력하세요')
    if a == 'stop':
        break