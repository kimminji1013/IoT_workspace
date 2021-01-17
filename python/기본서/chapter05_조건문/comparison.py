# 비교 연산자

country = "Korea"
if country == "Korea":
    print("South Korea")

if country != "Korea":
    print("No South Korea")

# 문자열의 경우, 왼쪽부터 문자 하나하나 비교
if "Korea" > "Japen":
    print("Korea win!")
else:
    print("Japen win!")

# 대문자와 소문자 사이에 특수기호 6개 존재
print(ord('Z'),ord('a')) # 90, 97