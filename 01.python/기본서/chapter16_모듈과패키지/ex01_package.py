# 모듈을 모아 놓은 디렉토리
# 반드시 __init__.py 파일이 존재해야 함
#   - 일반적으로 내용은 없음
from mypack.calc import add

add.outadd(1,2)


#__init__.py 파일에 넣을 수 코드 중 하나
# from A import * 에서 *를 한정지을 수 있는 코드
# __all__ = ["add","multi"]
# 거의 사용하진 않음
# 일반적으로는 비워 둠.
