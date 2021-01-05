# for 반복문
"""
for student in [1,2,3,4,5]:
    print(student,'번 학생의 성적을 처리합니다.')
    """

total = 0
for num in range (1,101):
    total += num

print("total =", total)

# for defalt 는 시작값이 0 증가값이 1
for a in range(5):
    print("Hi")


# ex01
for x in range(0,51):
    if x%10 == 0 or x==0:
        print("+", end='')
    else:
        print("-",end='')