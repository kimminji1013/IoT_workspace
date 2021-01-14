#  키워드 가변 인수
#  라이브러리 함수가 만들어지는 예시 (매개변수 제한X)
# def func(name, *arg, **arg): 
# name은 필수인수, *arg와 **arg는 가변 인수
# *는 list **는 dictionary
# 생략했을 때 디폴트 값을 갖기 위해선 get 함수 사용해야 함.
"""
def calcstep(**args):
    print(args)
    begin = args['begin']
    end = args['end']
    step = args['step']
    
    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total

print('3~5=',calcstep(begin=3, end=5, step=1))
"""

def calcscore(name, *score, **option):
    print(name)
    total = 0
    for s in score:
        total += s
    print("total:", total)
    if (option.get('avg',False)==True):
        print('avg:', total/len(score))
calcscore('김민지',99,88,77)#,avg=True)