import json


dic={'file_name' :'C:/Users/KMJ/Pictures/prideandprejudicemovieclip.jpg',
'file_size': 400500}

# 사전(파이썬 자료구조 객체)->문자열로 표현
msg = json.dumps(dic)   # json.dump()
print(type(msg),msg)



# 문자열 msg를 수신
# 문자열 --> 사전 객체로 복원
dic2 = json.loads(msg)  # json.load()는 파일 대상, loads는 문자열 대상
print(type(dic2))
print(dic2)