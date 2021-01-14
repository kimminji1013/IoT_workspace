# 스레드는 두 방법으로 실행
# 1. 함수 2.상속

# 함수로 표현하기 : threading module 이용
import threading

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print('Subthread', total)

t = threading.Thread(target=sum, args=(1,100))
t.start()  # 이 명령어를 해야 subthread 생성!

print("Main Thread")

# > Subthread Main Thread 4950 
# CPU 성능에 따라 순서가 다 다르게 나온 것.
# 누가 먼저 끝날지는 모른다.. (◆ 왜 코드 순서에 따라 출력되지 않는 것인가?)