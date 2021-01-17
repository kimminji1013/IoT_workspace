# 예외 발생 여부와 상관 없이 항상 호출됨.
# 예를 들어, 통신 연결했으면, 중간에 오류가 나더라도
# 통신을 끊고 해결해야하는 경우

def Network():
    try:
        print('Network connect')
        #a=1/0  # 오류
        print('네트워크 수행') # 오류가 나면 수행하면 안되므로
    except:
        print('Error')
    finally:
        print('Network disconnect')
        # 오류가 나더라도 통신은 해제해야 함

print('Network start')
Network()
print('End')