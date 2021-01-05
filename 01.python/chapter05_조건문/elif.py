# 여러 개의 if 문으로 조건을 검사할 때 사용
# 중간에 하나라도 참이 결정되면, 뒤에 다른 비교는 하지 않음

age = int(input("how old are youu?"))
if age<19:
    print("forbidden")
elif age<25:
    print("graduated")
else:
    print("come in!")


