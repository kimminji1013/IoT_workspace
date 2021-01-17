# 뒤에서 자세히 배울 것임. 기본만
# Tuple은 읽기 전용임. list 처럼 값 수정, 변경, 추가 불가

member = ('엄마','아빠','언니','나')
print(type(member))
print(member)

for ii in range (0,4):
    print(member[ii], end=' ')
    