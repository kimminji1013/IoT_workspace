# 리스트의 사본
# 리스트는 일반 변수와 달리, 원본 하나로 작업이 이루어진다.
# 사본에 값을 변경하면 원본 값도 변경 됨.

# 변수는 참조형과 일반형이 있다.
# list를 보통 '참조형'(reference) 라고도 부른다.
# 실제 데이터는 다른 곳에 있고, 변수들은 그 메모리를 참조하고 있다로 이해해야 함.

# list의 element 자체를 바꿀 땐,  list1, list2 같이 바뀜.
"""
list1 = [1, 2, 3]
list2 = list1

list2[1] = 100
print(list1)
print(list2)
print(list1 == list2)
"""
# 문자 아니고 문자열!에 대한 것임. 
# str의 element 아니고, 참조하는 변수를 바꿀 땐 list2만 바뀜.
str = 'Hi im minji'
str2 = str
print(str, str2)
str2 = "Bye"
#str2[0] = 'h'    #----> 문자열에서는 element 기능을 수행하지 않음. 
print(str, str2)   #----> 참조 요소가 아니라 참조 변수(화살표) 자체가 가리키는 메모리 변수가 바뀐 것.
                    #따라서 str2 만 바뀜.



# 얕은 복사, 깊은 복사
"""
import copy # 깊은 복사의 copy를 위해
list0 = ['a','b']
list1 = [list0,1,2]
list2 = list1.copy() #얕은 복사

list2[0][1] = 'c'
print(list1)
print(list2)

list3 = ['a', 'b']
list4 = [list3, 1, 2]
list5 =copy.deepcopy (list4) # 깊은 복사
list5[0][1] = 'c'
print(list4)
print(list5)
"""