# list
# ,로 값을 구분.
# 값들을 제거하거나, 추가, 수정할 수 있음
member = ['아빠','엄마','언니','나']
print(type(member))
print(member)

# 출력 시 대괄호로 묶여 있기 때문에 list임을 알 수 있음.
#print(member[0])

for i in range (0,4):
    print(member[i],end=' ')
