url = "https://www.naver.com/blog/travel/seoul.html"

'''
# 분리 전
print(url[0])
# 분리 후
els = url.split("://")
print(els)
print(els[0])
print(els[1])
'''

# 분할
trabler = """
강가루 건너서
밀밭 길을

구름에 달 가듯이
가는 나그네
"""

poet = trabler.splitlines()
print(poet)
for line in poet:
    print(line)
