
"""
nums = [11, 22, 33]

it = iter(nums)

# for문의 내부 메커니즘
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)
"""
# 제너레이터
"""
def seqgen(data):
    for index in range(0,len(data),2):
        yield data[index:index+2]
Hanguel = seqgen("가나다라마바사아자차카타파하")
for k in Hanguel:
    print(k, end=',')
"""

# 지역 함수
"""
def calcsum(n):
    def add (a,b):
        return a+b
    total = 0
    for i in range(n+1):
        total = add(total,i)
    return total

print(f"~10 = {calcsum(10)}")
"""
# 함수를 리턴
"""
def makeHello(message):
    def hello(name):
        print(message +', '+name)
    return hello

enghello = makeHello('Good Morning')
kohello = makeHello('안녕하세요')

enghello('Mr Kim')
kohello('김민지')
"""
#함수 데코레이터
"""
def inner():
    print('결과를 출력합니다.')

def outer(func):
    print('-'*20)
    func()
    print('-'*20)

outer(inner)

def hello():
    print('안녕하세요.')

outer(hello)
"""

# 함수 데코레이터 개선
# 실행하고싶은건 inner함수인데, 실제 함수 실행은 outer라서 불편-
"""
def inner():
    print("함수를 출력합니다.")

def outer(func):
    def wrapper():
        print('-'*20)
        func()
        print('-'*20)
    return wrapper

# 함수를 리턴하므로 inner()가 가능한것
# 밑에처럼 짜면 inner() 안됨
    # print('-'*20)
    # func()
    # print('-'*20)
inner = outer(inner)
inner()
"""

# 데코레이터 @ 사용
def outer(func):
    # def wrapper():
    #     print('-'*20)
    #     func()
    #     print('-'*20)
    # return wrapper
#---------------------------
    print('-'*20)
    func()
    print('-'*20)

@outer
def inner():
    print("함수를 출력합니다.")
# wrapper() 넣으면 inner()로 출력
inner
