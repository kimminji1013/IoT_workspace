# class = 객체(object)를 정의한다.
# class 이름은 관례로 첫 글자를 대문자로, 복합단어는
# _ 없이 첫글자는 대문자로! ex) AccountForCity
# 객체를 구분하기 위해서 instance를 사용. 

# class는 내에서의 함수는 method(메서드)라고 부른다.
# __???__ 이렇게 under bar 2개를 앞뒤로 붙은 이름은 파이썬에서 만든 것.
"""
class Account:
    def __init__(self, balance):    # 생성자 함수
        self.balance = balance      # self는 파이썬이 넣어주는 값. 
                                    # 개발자는 balance에 값 넣어주는 것
    def deposit(self, money):
        self.balance += money
    
    def inquire(self):
        print(f'잔액은 {self.balance}원 입니다.')

account = Account(8000) # Account 클래스가 시작하면서 heap을 할당받고, 
                        # 그 heap의 첫 인스턴스의 참조값이 account에 저장.
                        # 여기서는 첫 인스턴스에 8000이란 값 넣었고, 그 값의
                        # 주소값을 account에 저장하는 것.
account.deposit(1000)
account.inquire()
"""
"""
li1 = [1,2,3]
li1.append(12) # ctrl + method =  method의 정의 보여줌.
"""


# 생성자 예시
"""
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(str(self.age) + '살 ' + self.name +'입니다.')

kim = Human('김민지',28)
kim.intro()

lee = Human('이이이',50)
lee.intro()
"""


# 생성자 내부 아니어도 참조변수 추가 가능
"""
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change(self, gender):
        self.gender = gender

    def intro(self):
        print(str(self.age) + '살 ' + self.name + self.gender + '입니다.')

kim = Human('김민지',28)
# kim.intro()
# kim.gender = '남'  #attribute는 고정된 것이 아님. 확장,제거 가능
kim.change('남')
kim.intro()
"""


# 참조변수 값을 단순 확인 위해 메소드 추가
# print(kim) 하면 값이 아니라 주소값이 나옴
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = None

    def change(self, gender):
        self.gender = gender

    def intro(self):
        print(str(self.age) + '살 ' + self.name + self.gender + '입니다.')
#****************************************************************
    def __str__(self):  # 파이썬이 관리하는 특수 매소드
        return f'<Human {self.age}, {self.name}, {self.gender}>' # 이 함수를 넣어줌으로써 값 확인
#****************************************************************
    def __repr__(self):
        return f'<Human {self.name}>'
#****************************************************************


kim = Human('김민지',28)
lee = Human('이이이',50)
lee.change('여')
kim.change('남')
# print(kim) #특정 instance에 대해 자세히 보겠다.
# print(lee)

li = [kim, lee]  # 요소로서 출력은 축약버전으로 출력됨. 요소의 일부로
                 # 출력될 땐 __ str__아니고 __repr__이 사용됨
print(li)