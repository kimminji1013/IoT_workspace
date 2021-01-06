# 집합
# 값의 중복을 허용하지 않음 'key 값을 다룰 때 사용'
# 중복을 허용하지 않으므로 이미 값이 있으면 추가하지 않음

# {}--> 사전, set{}--->집합

set1 = set(range(2,13,2))
set2 = set(range(3,16,3))

print('합집합 :', set1 | set2)
print('차집합 :', set1 - set2)
print('차집합 :', set2 - set1)
print('배타적 차집합 :', set1 ^ set2)