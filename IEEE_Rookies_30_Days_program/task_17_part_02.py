if __name__ == '__main__':
    n = int(input(" enter number of bottles: "))
    v = []
    c = []
    for __ in range(n):
        x, y = map(int, input().split())
        v.append(x)
        c.append(y)

    max_1 = max(c)
    c.remove(max(c))
    max_2 = max(c)
    total_max = max_1 + max_2
    sum_v = sum(v)
    if total_max >= sum_v:
        print('Yes')
    else:
        print('No')

    input('press enter to exit...')



