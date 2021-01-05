def calcstep(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']

    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total

print("3~5 = ", calcstep(begin=3, end=5, step=1))