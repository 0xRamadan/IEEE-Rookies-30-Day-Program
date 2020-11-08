if __name__ == '__main__':

    n, t = map(int, input().split())
    l = list(map(int, input().split()))
    c = 0
    m = 0
    for i in range(n):
        c += 86400 - l[i]
        if c < t:
            m += 1
        elif c >= t:
            m += 1
            break
    print(m)

    input('press enter to exit...')
