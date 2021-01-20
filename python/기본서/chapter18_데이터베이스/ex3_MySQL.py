# python으로 MySQL/MariaDB 다루기 위해
# 현재 (base) 환경에 pip install mysqlclient  다운했음.
# heidi 접속 후 새 계정 설정 (계정 이름: iot, 비밀번호: 이전과 같음)




import MySQLdb

db = MySQLdb.connect (db ="employees", host = "localhost", user="iot", passwd ="3432")
# 하지만, APP 영역(python처럼)에서는 root 계정 굉장히 위험. 새로 만드는게 좋음
c = db.cursor()

# cursor로 MariaDB SQL 실행
query = "select * from departments"
c. execute(query)

rows = c.fetchall()
for no, name in rows:
    print(f"{no},{name}")



c.close()
db.close()