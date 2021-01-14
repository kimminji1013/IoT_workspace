# .find(str): str 문자열을 찾아 인덱스 반환 , 없으면 1 반환
# .rfind (str): 뒤에서 str 문자열을 찾아 인덱스 반환 , 없으면 1 반환
# .index(str): 와 동일 , 없으면 예외 발생
# .count(str): str 문자열이 몇번 등장하는지 리턴

s = 'python programming'
print(len(s))
print(s.find('o'))
print(s.rfind('o'))
print(s.index('r'))
print(s.count('o'))


# 단어 in 문자열 --> bool
# 단어 not in 문자열 --> bool
# startswith (str) --> bool
# endswith (str) --> bool

l = "python programming"
print('a' in l)
print('z' in l)
print('pro' in s)
print('x' not in s)