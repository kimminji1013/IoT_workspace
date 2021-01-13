nums = [11, 22, 33]

it = iter(nums)

# for문의 내부 메커니즘
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)
