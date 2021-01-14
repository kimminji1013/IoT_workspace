# 문자열 관리는 데이터를 조작하는 방법에 대해 배운다.
# 문자열, list, tuple, 사전 등등
"""
s = "0123456789"
print(s[2:5])
print(s[3:])
print(s[:4])
"""
"""
file = "20200101-104830.jpg"
print("촬영 날짜" + file[4:6]+"월"+file[6:8]+"일")
print("촬영 시간" + file[9:11]+"시"+file[6:8]+"분")

socialnum = '001212-34511231'
"""
#'생년-월-일'로 포맷팅 해서 출력
# 출신 지역 코드 출력

socialnum = '001212-34511231'

year = socialnum[:2]
month = socialnum[2:4]
date = socialnum[4:6]
region = socialnum[8:10]
letter_7 = socialnum[7]


if letter_7 == ('1' or '2'):
    year = '19'+year
else:
    year = '20'+year

print(letter_7)
print("생일:", year+'-'+month+'-'+date)
print("지역 코드:", region)
