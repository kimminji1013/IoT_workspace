# isalpha
# islower
# isupper
# isspace
# isalnum
# isdecimal
# isdigit
# isnumeric
# isidentifier
# isprintable

# 데이터에는 항상 오류가 있을 것이라고 판단할 것!

height = input("height : ")
if height.isnumeric(): # true면 1 , false명 0
    print("height : ", height)
else:
    print("only numeric number please")