# 정적 메소드
# 단순히 클래스 내에 정의되는 일반 함수
# 클래스에 대한 정보 제공 X
# 첫 번째 인자가 정해져 있지 않음

# 비슷한 성격의 함수를 묶어서 관리하기 위함

class Car:
    @staticmethod
    def Hello():
        print('안전 운전 합시다.')

    count = 0

    def __init__(self, name):
        self.name = name
        Car.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)

Car.Hello()