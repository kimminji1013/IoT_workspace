# if문은 true/false

age = int(input("how old are you?"))
# input의 defalt 는 str임! 형변환 항상 생각해 줘야 함.

if age <19: #:은 들여쓰기 시작으로 생각하면 됨
    print('forbidden')
else:
    print('accept')

# 들여쓰기 할 때, tab 보다는 space bar 공백 선호
# tab과 spacebar 크기가 다르기 때문에 혼선의 여지 존재