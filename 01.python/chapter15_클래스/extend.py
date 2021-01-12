# 상속 inheritance 사용 안하고 extend 를 사용
# 기존 클래스 정의를 그대로 자신의 것으로 취하는 방법

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age) + '살' + self.name + "입니다.")


class Student(Human):
    def __init__(self, name, age, stunum):
        super().__init__(name, age)
        self.stunum = stunum

    def intro(self):   # 부모 함수 이름 따라하기 (override)
        super().intro()   
        print('학번:' +str(self.stunum))
    # 만약 학생 intro 메소드 없이 lee.intro() 출력한다면 
    # class 에서 부모것 가져왔으므로 부모의 intro만 출력된다.
    def study(self):
        print('ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ')