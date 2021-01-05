# 함수의 도움말
# help(함수명) 호출 시 출력될 문자열
# """ 로 문자열 설명

def calcsum(n):
    """1~n 까지의 합계를 구해 리턴한다."""
    total = 0
    for i in range (n+1):
        total += i
    return total

help(calcsum)