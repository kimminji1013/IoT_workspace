# 문제
# 컴퓨터와 가위바위보를 해서 승자 판정
# 컴퓨터는 랜덤하게 결정
# 사용자는 input으로 값 입력

# 가위:1 바위:2 보:3 라고 표현 설정
import random
game = ['scissor','rock','paper']
game_num = [1,2,3]
me = int(input("scissor(1)-rock(2)-paper(3)?\
    please input the number"))
computer = random.choice(game_num)


"""if computer == 1:
    if me == 2:
        print('I win!')
    elif me==3:
        print('Computer win!')
    else:
        print('draw!')
elif computer == 2:
    if me == 3:
        print('I win!')
    elif me==1:
        print('Computer win!')
    else:
        print('draw!')
elif computer == 3:
    if me == 1:
        print('I win!')
    elif me==2:
        print('Computer win!')
    else:
        print('draw!')"""


print(computer)

if computer == me:
    print('draw!')
elif computer == 1:
    if me == 2:
        print('I win!')
    elif me==3:
        print('Computer win!')
elif computer == 2:
    if me == 3:
        print('I win!')
    elif me==1:
        print('Computer win!')
elif computer == 3:
    if me == 1:
        print('I win!')
    elif me==2:
        print('Computer win!')



print(computer)