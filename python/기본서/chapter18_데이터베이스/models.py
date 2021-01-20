# fetch로 불러온 데이터는 튜플이다. 사용하려면 return[0], return[1] 이런식으로 사용해야 하는데,
# 무엇을 뜻하는지 가독성이 떨어지므로 리스트로 바꿔 return.num, return.name 이렇게 사용하려고 만든 클래스


# 모델 객체 : 로직 없이 데이터만 관리는 클래스
class AddressBookEntry:
    def __init__(self, num, name, phone, email, addr):
        self.num = num
        self.name = name
        self.phone = phone
        self.email = email
        self. addr = addr



    def __str__(self):
        return f'<AddressBookEntry {self.num}, {self.name}, {self.phone}, {self.email},{self.addr}>'
    def __repr__(self):
        return f'<AddressBookEntry {self.num}, {self.name} >'