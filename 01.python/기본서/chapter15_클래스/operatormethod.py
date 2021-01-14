# 연산자 별로 함수명이 정해져 있음.



class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
kim = Human("김민지",28)
minji= Human("김민지",28)
ga = Human('김가연',31)

print(kim == minji)
print(kim == ga)

# def __eq__(self, other) 없으면, kim과 minji가 참조하는 인스턴스
# 주소가 다르므로 출력은 False