# sys.exit(0) : 더이상 프로그램 진행할 필요 없을 때 바로 종료시켜 줌.
import sys

while True:
    ans = input('command')
    if ans == 'quit':
        sys.exit(0)

    print(ans)

    # exit() 의 매개변수는 개발자가 정함
    # ex) 1 : 메모리 부족, 2: 데이터 오류.....
    # 관례적으로 0은 정상적인 종료를 뜻 함.