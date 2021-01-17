SCISSORS = 1
ROCK = 2
PAPER = 3
# 대문자로 변수 설정한 건, 상수로 생각해달라는 관례

import random

game_num = [1,2,3]
user = int(input("scissor(1)-rock(2)-paper(3)?\
    please input the number"))
computer = random.choice(game_num)

if user == computer:
    print('draw!')
elif user == SCISSORS and computer == PAPER:
    print('I win!', 'computer =', computer, 'user = ', user)
elif user == ROCK and computer == SCISSORS:
    print('I win!', 'computer =', computer, 'user = ', user)
elif user == PAPER and computer == ROCK:
    print('I win!', 'computer =', computer, 'user = ', user) 
else:
    print('Computer win!', 'computer =', computer, 'user = ', user)