# 분할
# split(구분자) : 구분자 기준으로 단어를 분리해 리스트로 리턴
# 결합문자열.join(문자열)

s = 'red blue yellow green pink purple'
print(s.split())
s2 = 'red-> blue->yellow->green->pink->purple'
print(s2.split('->'))


#print(s2.strip().split('->'))
s2=s2.replace(" ","")
print(s2.split('->'))