import MySQLdb
import time
from app_base_db import Application
from dao import AddressBookDao




class AddrBookApp(Application):
    def __init__(self):
        super().__init__()
        print(self.config)
        # 초기화 작업
        # db는 utf-8인데, MySQLdb는 아니므로 지정해줘야 함
        self.db = MySQLdb.connect(host=self.config['host'],
                                db = self.config['db'],
                                user = self.config['user'],
                                passwd = self.config['passwd'],
                                charset="utf8", use_unicode=True)
        
        self.cursor = self.db.cursor()
        # 데이터의 양이 너무 많아 한번에 출력할 갯수를 정해준다. 
        # 대문자로 변수를 지정한 건 앞으로 이 상수값으로 사용하겠다는 관례다.
        self.PERPAGE = 20
        self.addrbook_dao = AddressBookDao(self.cursor)


    def create_menu(self,menu):
        menu.add('목록',self.print_list)
        menu.add('상세보기',self.print_detail)
        menu.add('검색',self.search)
        menu.add('추가',self.add)
        menu.add('수정',self.update)
        menu.add('삭제',self.delete)
        menu.add('종료',self.exit)


    def print_list(self):
        page = int(input('page : '))
        pagination = self.addrbook_dao.get_page(page, self.PERPAGE)
        print('='*100)
        for e in pagination.data:
            print(f"{e.num:8d}. 이름:{e.name:22s} 전화:{e.phone:13s}  이메일:{e.email:20s} 주소:{e.addr}") # ◆ e.으로 바뀐것 이해안됨
        print('-'*100)
        print(f'{page}/{pagination.total_page} (총:{pagination.total_count}건)')
        print('-'*100)
        time.sleep(1)


    def print_detail(self):
        num = int(input('number : '))
        row = self.addrbook_dao.get(num)

        # 잘못된 번호를 입력했을시, None 반환되므로 검사해줘야함
        if not row: # None이라면 
            print(f'{num} 데이터가 없습니다.')
            return

        print('='*100)
        print(f'No.:{row.num}')
        print(f'이름:{row.name}')   
        print(f'전화번호:{row.phone}')   
        print(f'이메일:{row.email}')   
        print(f'주소:{row.addr}')   
        print('-'*100)
        time.sleep(1)


    def search(self):
        keyword = input('keywords : ')
        rows = self.addrbook_dao.search(keyword)
    
        print('='*100)
        print(f'검색 결과({keyword})')
        print('-'*100)
        for e in rows:
            print(f"{e.num:8d}. 이름:{e.name:22s} 전화:{e.phone:13s}  이메일:{e.email:20s} 주소:{e.addr}")
        print('-'*100)
        time.sleep(1)


    def add(self):
        pass
    

    def update(self):
        pass
    
    
    def delete(self):
        pass
    

    # cleanup 작업
    def destroyed(self):
        self.cursor.close() 
        self.db.close() 

if __name__ == "__main__":
    app = AddrBookApp()
    app.run()