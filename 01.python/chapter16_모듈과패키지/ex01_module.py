# 파일명이 모듈의 이름이 된다.
# import A : A 모듈을 임포트
#       -> 사용할 때, A.(def명)
# from A import * : A 모듈의 모든 요소를 임포트하겠다.
#       -> 사용할 때, (def명)
# 이처럼 바로 사용 가능하지만 이름 충돌될 가능성이 높아져 조심해야 함.


# __name__으로 현재 파일이 모듈인지, 실행 주체인지 확인
"""
import m1

if __name__ =="__main__":
    print(m1.calcsum(10))

print('module.py')
"""

# 모듈의 내부 확인하기
# 모듈 내부에 존재하는 함수 목록 list로 출력
"""
import sys
print(sys.builtin_module_names)
"""

import math
print(dir(math))
print(math.__file__)