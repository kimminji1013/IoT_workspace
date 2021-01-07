# .random() : 0~1(1은 포함x) 사이의 난수 리턴.
# 소수점 이하 16자리 난수

# randint(begin, end) :  begin~end 사이 정수 난수 리턴(end 포함)
# randrange(begin, end) :  begin~end 사이 정수 난수 리턴(end 미포함)
# uniform(begin, end) :  begin~end 사이 실수 난수 리턴(end 미포함)
# random.choice(sequence) : sequence에서 랜덤하게 하나 뽑음
# rand.shuffle(sequence) : sequence 랜덤하게 섞음
# rand.sample(range(begin, end),count) : 범위내 랜덤하게 count 갯수 출력

import random

food = ['Korean food','Japenese food','Chinese food']
print(random.sample(food,2))
