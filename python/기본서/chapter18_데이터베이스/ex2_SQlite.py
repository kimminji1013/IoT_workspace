import sqlite3
 
con = sqlite3.connect('addr.db')
cursor = con.cursor()

# update
m_name = input("추가할 이름을 입력하세요 : ")
m_phone = input("추가할 번호를 입력하세요 ex) 010-0000-0000) : ")
m_addr = input("추가할 주소를 입력하세요 : ")
add_info = f"INSERT INTO tblAddr VALUES('{m_name}', '{m_phone}', '{m_addr}')"
cursor.execute(add_info)
con.commit()


#delete
d_name = input("삭제할 이름을 입력하세요 : ")
del_info = f"DELETE FROM tblAddr WHERE name = '{d_name}'"
con.commit()

#update
# u_name = input("수정할 이름을 입력하세요 : ")
# up_info = f"DELETE FROM tblAddr WHERE name = '{u_name}'"
# table = cursor.fetchall()
# print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")
# for name, phone, addr in table:
#     print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")


con.commit()


# search
name = input("주소를 검색할 이름을 입력해 주세요 : ")
query = f"SELECT addr FROM tblAddr WHERE name = '{name}'"
cursor.execute(query)
            
record = cursor.fetchone()
print(type(record), record)

if record : print(f"{name}은/는 {record[0]}에 살고 있습니다.")
else : print (f"{name}은/는 없는 이름입니다.")     

cursor.close()
con.close()