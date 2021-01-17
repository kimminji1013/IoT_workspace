# Formatting
# %d 정수
# %f 실수
# %s 문자열
# %c 문자 하나
# %h 16 진수
# %o 8 진수 # %% % 문자
# 폭 유효자리수 서식 , 폭에는 소수점에 포함 , 반올림 발생

name = "민지"
age = 28
height = 162.5
print("이름:{}, 나이:{}, 키:{}".format(name, age, height))

print("이름:{:4s}, 나이:{:3d}, 키:{:.2f}\n".format(name, age, height))

# python 3.7 부터 지원하는 방법 f-string
print(f"이름:{name}, 나이:{age}, 키:{height}")
print(f"이름:{name:4s}, 나이:{age:3d}, 키:{height:.2f}\n")