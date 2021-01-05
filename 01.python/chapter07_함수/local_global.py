# 지역변수 전역변수
"""
def kim():
    temp = "function of kim"
    print(temp)
temp = "Hello"
kim()
print(temp)
"""

"""
def kim():
    temp = "function of kim"
    print(temp)

def lee():
    temp = "function of lee"
    print(temp)

def park():
    temp = "function of park"
    print(temp)    

kim()
lee()
park()
"""

# 전역변수
"""
salerate = 0.9

def kim():
    print("today salerate is :", salerate)

def lee():
    price = 1000
    print("price :", price * salerate)

kim()
salerate =1.1
lee()
"""

# 지역/전역 변수 frame id 확인
"""
price = 1000
def sale():
    price = 500
    print("sale price :", price, "\tlocal id :", id(price))

sale()
print("price :", price, "\tglobal id :", id(price))
"""

#전역 변수를 함수에서 사용 

price = 1000
def sale():
    global price 
    price = 500
    print("sale price :", price, "\tlocal id :", id(price))

sale()
print("price :", price, "\tglobal id :", id(price))