# 주소록 앱 ---> 객체 지향적으로 만들기
# 코드짜기 전에 필요한 객체 뭔지 구분할 것.
"""
1. 문제파악
2. 필요한 객체
2-1. 어떤 정보를 다루는가? 
    1) 이름/이메일/전화번호/주소
    2) 설정 정보 (주소록 파일명, 인코딩 setting 등등)
2-2. 단일 데이터의 형태는 어떠한가?
    1) 하나의 주소록 정보 : 이름, 이메일, 번호, 주소 --> 한 쌍으로 단위 데이터
    2) 파일명, 인코딩 setting 정보 ---> 한 쌍으로 단위 데이터
2-3. 데이터의 갯수, 어떻게 관리할 것인가?
    1) 주소록 : N개 (컬렉션으로 관리) 
    2) 설정 정보 : 1개 (단일 변수로 관리)
"""

# 모델 객체 : 정보(데이타)만을 저장하는 Class 
class Configuration:
    def __init__(self):
    #csv 파일 경로명, encoding --> 매개변수 입력 받는 것이 아니라 설정 파일 정보를 가져옴
        config = self.load()
        self.fname = config['FNAME']
        self.encoding = config['ENCODING']
    
    def load(self):
        config={}
        with open('config.ini','rt') as f:
            entries = f.readlines()
            for l in entries:
                key, value = l.split('=')
                config[key.strip()] = value.strip()
        return config
        
    def __str__(self):
        return f'<Configuration fname:{self.fname}, encoding:{self.encoding}>'

# 모델 객체
class AddressBookEntry:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self. addr = addr

    def __str__(self):
        return f'<AddressBookEntry {self.name}, {self.phone}, {self.email},{self.addr}>'
    def __repr__(self):
        return f'<AddressBookEntry {self.name} >'

# config = Configuration()
# entry = AddressBookEntry('김민지','010-1111-1111','mj@mail','서울')
# print(entry)
# print([entry])



# 여러개의 주소록 entry 관리가 목적
# 사전은 이름을 key로 해서 동명이인 처리 불가
# 여기서는 리스트로 처리하겠음.
class AddressBook:  
    def __init__(self):
        self.book = []

    def load(self, config):
        with open(config.fname, 'rt', encoding=config.encoding) as f:
            lines = f.readlines()[1:] # ◆ 함수 호출 하고 슬라이싱으로 헤더 제외 
            for line in lines: 
                name, phone, email, addr = line.split(',')
                addr = addr.strip()
                entry = AddressBookEntry(name, phone, email, addr) # ◆
                self.book.append(entry)
        
        # 이름순으로 정렬
        # a 가 AddressBookEntry 이므로 그 중 이름으로 정렬하겠다.
        self.book.sort(key=lambda a:a.name) # ◆

    # 추가
    def add(self, name, phone, email, addr):
        pass

    # 삭제
    def delete(self, name):
        pass

    # 수정
    def update(self, name, phone, email, addr):
        pass


    def __str__(self):
        return f'<AddressBook {self.book}>'

# config = Configuration()
# book = AddressBook()
# book.load(config)
# print(book)



# Configuration :  설정 정보 담당
# AdressBookEntry : 한 사람의 주소 정보 담당
# AdressBook : 목록 관리
class Application:
    def __init__(self):
        self.config = Configuration()
        self.addressbook = AddressBook()
        self.addressbook.load(self.config)

    def select_menu(self):
        print('1. 목록', '2. 상세보기','3. 추가', '4. 수정', '5. 삭제','6. 종료',sep='\n')
        menu = int(input('입력:'))
        return menu
        
    def run(self,menu):
        if menu == 1: #목록
            self.print_book()
        elif menu == 2: #상세보기
            self.print_detail()
        elif menu == 3: #추가
            self.add()
        elif menu == 4: #수정
            self.update()
        elif menu == 5: #삭제
            self.delete()
        elif menu == 6: #종료
                #sys.exit(0) 그냥 시스템 종료
            self.exit()
        else:
            print('Wrong number')

    
    def print_book(self):
        print("="*50)
        print('주소록')
        print("="*50)
        for index, entry in enumerate(self.addressbook.book):
            print(f'{index:02d}),{entry.name}:{entry.phone},{entry.email},{entry.addr}')
    
    def print_detail(self):
        pass

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def exit(self):
        pass

def main():
    app = Application()
    while True:
        menu = app.select_menu()
        app.run(menu)


main()

