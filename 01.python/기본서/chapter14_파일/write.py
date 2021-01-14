# 파이썬에서는 깨져서 보이지만, 파일로 들어가면 제대로 보임. 
# 파이썬에서는 UTF-8 이라는 유니코드로 해석 
# 파이썬의 defalt 는 UTF-8
# 메모장은 ASCI라는 아스키 코드로 해석
# 참고로 window는 CP949(EUC-KR)


# 파일->다른 이름으로 저장-> UTF-8로 변경 (문자set 변경하면 됨)

# f = open('live.txt','wt')
f = open('live.txt','wt', encoding='utf-8')
f.write("""난 너를 사랑하네
이세상은 너뿐이야
""")
f.write('''추가한 내용입니다.''')

f.close()

# 'at'는 기존꺼에 추가로 쓰기

#  f = open('live.txt','at', encoding='utf-8')
#  f.write("""난 너를 사랑하네
#  이세상은 너뿐이야
#  """)
#  f.close()

