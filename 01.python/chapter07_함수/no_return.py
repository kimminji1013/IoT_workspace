def printsum(n):
    total = 0
    for num in range(n+1):
        total += num
    print("~",n,"=",total)


  # ~4=10 출력되지만, None 같이 출력
  # 변수에 지정은 리턴 값이 있어야만 가능.
"""
a = printsum(4)
print(a)
"""