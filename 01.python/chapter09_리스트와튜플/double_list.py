# 이중 리스트
import random
"""
double_list = [
    [1,2,3],
    [4,5],
    [6,7,8,8]
]

for sub in double_list:
    for item in sub:
        print(item, end=' ')
    print()
"""

# 학생별 과목별 점수
score=[
    list(random.sample(range(70,100),4)),
    list(random.sample(range(70,100),4)),
    list(random.sample(range(70,100),4))
]

total_s = 0
total_sub = 0

for student in score:
    student_total = 0
    for subject in student:
        student_total += subject
    subjects = len(student)
    print(f'total_per_student:{student_total}',\
        f'average_per_student:{student_total/subjects}')
    total_sub += student_total
    total_s += subjects
print(f'total_average:.{(total_sub/total_s):.2f}')
