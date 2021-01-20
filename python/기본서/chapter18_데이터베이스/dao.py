# 이 파일은 addressbook_db 에서 데이터를 처리해주는 객체를 만들 파일입니다.
# dao = data of objects : 객체의 데이타 처리를 전담하는 것.
import math
from models import AddressBookEntry


# page 운영에 필요한 객체
class Pagiation:
    def __init__(self, total_count, total_page, data):
        self.total_count = total_count
        self.total_page  = total_page
        self.data = data


class AddressBookDao:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_total_count(self):
        query = f'SELECT COUNT(*) FROM addressbook'
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    # 페이지에 들어가는 데이터를 꺼내는 일만
    def get_list(self, start, perpage):
        query = f"SELECT * FROM addressbook ORDER BY name LIMIT {start},{perpage}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()  #데이터가 있으면 ((,,..)..) 튜플안에튜플로 표현, 없으면 () 빈튜플 반환
        # 1.comprehension을 이용했을 때
        return (AddressBookEntry(*row) for row in rows) # 괄호 대신 대괄호면 리스트로 만들겠다는 뜻.


    # pagination을 구성하고 리턴해주는 걸로   
    def get_page(self, page, perpage):
        start = (page-1)*perpage
        total_count = self.get_total_count()
        total_page = math.ceil(self.get_total_count()/perpage)
        rows = self.get_list(start, perpage)
   
        return Pagiation(total_count, total_page, rows)    

    def get(self, num):
        query = f'select * from addressbook where num={num}'
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        if row:
            return AddressBookEntry(*row)  #AddressBookEntry의 input 순서와 동일하다는 가정하에 *사용
        else:
            return None
            

    def search(self,keyword):
        keyword = keyword.lower()   # 데이터 대소문자 구분하므로, 구분 안하고 검색하기 위해
        query = f"SELECT * FROM addressbook WHERE lower(name) like '%{keyword}%'"  
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return (AddressBookEntry(*row) for row in rows)


    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
    
    
    pass