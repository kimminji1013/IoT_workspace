# 기존 리스트와 튜플은 순서(인덱스)로 관리한 반면,
# 사전은 순서는 상관 없고 key로 관리한다.

# 리스트에서는 요소를 element, 사전은 entry라 한다.
# {키:값} , key는 중복X , value는 여러개 가능

# .keys() : 키 목록 리턴
# .values() : 값 목록 리턴
# .items() :  (키, 값) 목록 리턴



# 예제1
# 순서는 상관 없다. 의미 없다!
"""
dic = {
    'boy':'소년',
    'girl':'소녀',
    'book':'책'
}
print(dic)
# 키가 존재하지 않을 때
print(dic['school']) #----> keyerror 발생

# 키가 존재하지 않으 때 get 사용
# 에러나서 전체 코드가 멈추지 않고 none으로 출력해 코드 돌아감.
print(dic.get('school'))
print(dic.get('school', 'no meaning'))
"""
"""
dic = {
    'boy':'소년',
    'girl':'소녀',
    'book':'책'
}
for i in dic:
    print(i, dic[i])
    """

# 사전 관리 
"""
dic = {
    'boy':'소년',
    'girl':'소녀',
    'book':'책'
}
dic['boy'] = '남자아이'
dic['girl'] = '여자아이'
del dic['book']
print(dic)
"""
# 사전 관리2
"""
dic = {
    'boy':'소년',
    'girl':'소녀',
    'book':'책'
}
print(dic.keys())
print(dic.values())
print(dic.items()) #---> 리스트 안에 튜플 3개 존재

# 튜플의 unpacking 기능을 이행해보자
for key, value in dic.items():
    print(key, value)
"""

# 사전 관리3
# 리스트에서는 추가할 때 + 또는 extend 사용
# 사전은 update 사용
# 키가 겹친 경우 뒤에 있는 매개변수 키 값으로 덮어 씌어짐
"""
dic = {
    'boy':'소년',
    'girl':'소녀',
    'book':'책'
}
dic2 = {
    'student':'학생',
    'school':'학교',
    'book':'교과서'
}
dic.update(dic2)
print(dic)
#print(dic.items())
"""

# 사전 관리4

li = [
    ('student','학생'),
    ('school','학교'),
    ('book','교과서')
]
dic = dict(li)
print(dic)




