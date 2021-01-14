# 주소록 앱 ---> 객체 지향적으로 만들기
# ex02 : 목록 추가를 자동으로 만들기
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
import time
import sys


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

    # 파일 저장
    # l = [1,2]--->','.join(l) = '1, 2' 문자열로 만들어주는 모듈
    def save(self, config):
        with open(config.fname, 'wt', encoding=config.encoding) as f:
            f.write('이름,전화번호,email,주소\n')
            for entry in self.book: # ◆
               # line = ','.join(entry)
                line = f'{entry.name},{entry.phone},{entry.email},{entry.addr}'
                f.write(line+'\n')


    # 이름 검색
    def search(self,keyword):
        result = []
        # for line in self.book:
        #     if line.name.fine(keyword) != -1:  # keyword를 포함한다면 (완벽히 맞지 않아도 됨.)
        #         result.append(line)
        # return result
        return list(filter(lambda line : line.name.find(keyword) != -1,self.book))
        
        


    # 추가
    def add(self, name, phone, email, addr):
        entry = AddressBookEntry(name, phone, email, addr)
        self.book.append(entry)
        self.book.sort(key=lambda a:a.name)


    # 삭제
    def delete(self, index):
        del self.book[index]
        

    # 수정
    def update(self, index, name, phone, email, addr):
        self.book[index].name = name
        self.book[index].phone = phone
        self.book[index].email = email
        self.book[index].addr = addr
        self.book.sort(key=lambda a:a.name)


    def __str__(self):
        return f'<AddressBook {self.book}>'

# config = Configuration()
# book = AddressBook()
# book.load(config)
# print(book)

class MenuItem:
    def __init__(self,title,func):
        self.title = title
        self.func = func

    def __str__(self):
        return f'<MenuItem {self.title}>'
    def __repr__(self):
        return f'<MenuItem {self.title} >'

#MenuItem을 관리하는 객체
class Menu:
    def __init__(self):
        self.menu_items = []

    def add(self, title, func):
        menu_item = MenuItem(title,func)
        self.menu_items.append(menu_item)

    def select_menu(self):
        for ix, menu_item in enumerate (self.menu_items,1):
            print(f'{ix}) {menu_item.title}',sep='\n')
        print()
        menu = int(input('번호를 입력해주세요 : '))
        return menu

    def run_menu(self, menu):
        if 1 <= menu <len(self.menu_items)+1: #리스트 검색 써도 되는지?
            menu_item = self.menu_items[menu-1]
            menu_item.func()
        else:
            print('메뉴 번호를 다시 한 번 확인해 주세요.')


# Configuration :  설정 정보 담당
# AdressBookEntry : 한 사람의 주소 정보 담당
# AdressBook : 목록 관리
class Application:
    def __init__(self):
        self.config = Configuration()
        self.addressbook = AddressBook()
        self.addressbook.load(self.config)
        self.menu = Menu()


        
        self.menu.add('목록', self.print_book)
        self.menu.add('상세보기', self.print_detail)
        self.menu.add('검색', self.search)
        self.menu.add('추가', self.add)
        self.menu.add('수정', self.update)
        self.menu.add('삭제', self.delete)
        self.menu.add('종료', self.exit)

    def run(self):
        while True:
            menu = self.menu.select_menu()
            self.menu.run_menu(menu)

    def print_book(self):
        print("="*50)
        print('주소록')
        print("="*50)
        for index, entry in enumerate(self.addressbook.book,1):
            # 동명이인 처리 위해 index 넣어줌
            print(f'{index:02d}){entry.name}:{entry.phone},{entry.email},{entry.addr}')
        print("-"*50)
        time.sleep(1)

    def print_detail(self):
        self.print_book()
        index = int(input('상세보기 할 번호를 입력해 주세요 : '))
        entry = self.addressbook.book[index-1]
        # print(entry)
        print(f'이름 : {entry.name}')
        print(f'전화번호 : {entry.phone}')
        print(f'이메일 : {entry.email}')
        print(f'주소 : {entry.addr}')
        time.sleep(2)

    # 검색방법 : 부분일치
    def search(self):
        keyword = input('검색어:')
        result = self.addressbook.search(keyword)
        print("="*50)
        print(f'검색 결과 : {len(result)}건')
        print("="*50)
        for index, entry in enumerate(result,1):
            print(f'{index:02d}) {entry.name}:{entry.phone},{entry.email},{entry.addr}')
        print("-"*50)
        time.sleep(1)
    
    
    def add(self):
        print('새 주소록 항목 추가')
        name = input('이름 :')
        phone = input('번호 : ')
        email = input('이메일 :')
        addr = input('주소 :')
        self.addressbook.add(name, phone, email, addr)
        print(f'{name}님 정보가 추가되었습니다.')
        time.sleep(2)

    def update(self):
        self.print_book()
        index = int(input('수정 할 번호를 입력해 주세요 : '))
        entry = self.addressbook.book[index-1]
        print('변경할 사항이 아니면 enter를 눌러주세요')
        name = input(f'이름 ({entry.name}):')
        if name.strip() == '':
            name = entry.name
        phone = input(f'번호 ({entry.phone}):')
        if phone.strip() == '':
            phone = entry.phone  
        email = input(f'메일 ({entry.email}):')
        if email.strip() == '':
            email = entry.email
        addr = input(f'주소 ({entry.addr}):')
        if addr.strip() == '':
            addr = entry.addr     
        self.addressbook.update(index-1, name, phone, email, addr)
        print('수정되었습니다.')
        time.sleep(1)

    def delete(self):
        self.print_book()
        index = int(input('번호를 입력해 주세요 : '))
        entry = self.addressbook.book[index-1]
        answer = input(f'{index}번 {entry.name}님 정보를 삭제하시겠습니까? [Y/N]')
        if answer == 'n'or answer =='N':
            print('메뉴로 돌아갑니다.')
            time.sleep(1)   
        elif answer == 'Y'or answer =='y':
            self.addressbook.delete(index-1)
            print(f'{index}번 정보가 정상적으로 삭제되었습니다.')
            time.sleep(1)

    def exit(self):
        answer = input('종료하시겠습니까? [Y/N]')
        if answer == 'n'or answer =='N':
            print('메뉴로 돌아갑니다.')
            time.sleep(1)   
        elif answer == 'Y'or answer =='y':        
            self.addressbook.save(self.config)
            sys.exit(0)


def main():
    app = Application()
    app.run()

main()

