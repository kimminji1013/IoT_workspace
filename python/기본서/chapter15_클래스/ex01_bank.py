# class.py의 계좌 class 확장
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def intro(self):
        print(str(self.age) + '살 ' + self.name + self.gender + '입니다.')

    def __str__(self):  # 파이썬이 관리하는 특수 매소드
        return f'<Human {self.age}, {self.name}, {self.gender}>' # 이 함수를 넣어줌으로써 값 확인

    def __repr__(self):
        return f'<Human {self.name}>'


class Account:
    def __init__(self, owner ,balance):    # 생성자 함수
        self.owner = owner
        self.balance = balance      # self는 파이썬이 넣어주는 값. 
                                    # 개발자는 balance에 값 넣어주는 것
    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        if self.balance < money:
            raise Exception ('잔액부족')  #raise는 예외 발생
            # Exception class의 instance를 만든다
        self.balance -= money
        return money

    def inquire(self):
        print(f'{self.owner}님의 잔액은 {self.balance}원 입니다.')



human_minji = Human('민지', 28, '여')
account = Account(human_minji,8000)
try:
    account.deposit(1000)
    account.withdraw(5000)
    account.inquire()
    # account.withdraw(5000)
    # account.inquire()
except Exception as e:
    print('오류 발생!\n원인:',e)
