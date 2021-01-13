# property를 사용할 땐, getter property를 먼저 만들어야, month property가 정의됨
# getter 함수는 read이므로 매개변수 받지 않음.



class Date:
    def __init__(self, month):
        self.inner_month = month

    @property
    def month(self):
        return self.inner_month

    @month.setter
    def month(self,month):
        if 1<= month <=12:
            self.inner_month = month

today = Date(8)
today.month = 15

print(today.month)