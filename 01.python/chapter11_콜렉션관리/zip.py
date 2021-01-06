# zip = 압축 아니고 모아준다는 뜻.(=archive)
# 짝이 맞는 한에서 만들어줌. element 갯수 다를 때
# 에러는 아니고 버림.
# 짝이 만들어진 것만 return (return값이 sequence이나 list는 아님.)
# zip은 loop 1번밖에 못씀! 그래서 처음부터 list로 변환시켜 사용


# 요일과 점심메뉴 zip
"""
dates = ['Mon','Tue','Wen','Thu','Fri','Sat','Sun']
food = ['갈비탕','순대국','칼국수','삼겹살','라면']

menu = list(zip(dates, food)) # list로 변환!
print(menu)
for d,f in menu:
    print(f'{d}메뉴 : {f}')
"""

# zip은 사전을 만들 때 사용
"""
dates = ['Mon','Tue','Wen','Thu','Fri','Sat','Sun']
food = ['갈비탕','순대국','칼국수','삼겹살','라면']

menu_dic = dict(zip(dates,food))
print(menu_dic)
"""
info = """고길동, 홍길동, 둘리, 도우너
30 40 50 60 
70 90 60 65 78 
80 100 20 90 100
30 40 50 60"""

info_split = info.splitlines()
student = info_split[0].split(', ')
#for re in student:
#    re = re.replace(',','')
#    re = re.extend(re)

scores = info_split[1:]
scores = [line.split() for line in scores]
info_dic = dict(zip(student, scores))
print(info_dic)




