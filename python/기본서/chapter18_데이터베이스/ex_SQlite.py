import sqlite3
 
con = sqlite3.connect('addr.db')
cursor = con.cursor()

# cursor.execute("SELECT * FROM tblAddr")

# select 전체 결과를 달라 : fetchall
# table = cursor.fetchall()
# for name, phone, addr in table:
#     print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

# cursor.close()
# con.close()


# 한 개의 행 추출, 추출후 내부적으로 다음행 이동 : fetchone
# while True:
#     record = cursor.fetchone()
#     if record == None:
#         break

#     print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

# cursor.close()
# con.close()
     


#WHERE 사용
import sqlite3
 
con = sqlite3.connect('addr.db')
cursor = con.cursor()
cursor.execute("SELECT addr FROM tblAddr WHERE name = '김민지'")
            # PK는 1개값만 존재 (없을수도 있음)
record = cursor.fetchone()
print(type(record), record)
if record : print(f"김민지는 {record[0]}에 살고 있습니다.")
else : print (f"김민지는 없는 이름입니다.")     

cursor.close()
con.close()