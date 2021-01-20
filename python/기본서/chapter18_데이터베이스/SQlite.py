# MariaDB보다훨씬 가벼운 파일기반 임베디드 데이터베이스
# 독립적인 DBMS 서버 대신 라이브러리 형태로 프로그램에 포함 운영
# 스마트폰에 들어있는 데이터베이스 모델

# python으로 SQLite 보는 법
# VS code 확장팩 'SQLite' 다운 _> f1검색 : SQLite: open data base
# -> 해당 파일 선택 -> 좌측 하단 ▶ 클릭!

import sqlite3

con = sqlite3.connect('addr.db')

cursor = con.cursor()

cursor. execute('Drop Table IF EXISTS tblAddr')

cursor.execute("""
CREATE TABLE tblAddr(
    name CHAR(16) pRIMARY KEY,
    phone CHAR(16),
    addr TEXT
)
""")

cursor.execute("INSERT INTO tblAddr VALUES('김민지', '010-2755-3432', '서울')")
cursor.execute("INSERT INTO tblAddr VALUES('김가연', '010-9480-3432', '서울')")
cursor.execute("INSERT INTO tblAddr VALUES('김래성', '010-5368-3432', '춘천')")
cursor.execute("INSERT INTO tblAddr VALUES('엄명화', '010-9057-3432', '춘천')")

con.commit()

cursor.close()
con.close()
