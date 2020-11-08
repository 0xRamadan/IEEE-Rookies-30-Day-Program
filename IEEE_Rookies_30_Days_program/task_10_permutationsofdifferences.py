def stones(n, a, b):
    res = set()
    if a > b:
        a, b = b, a

    for i in range(n):
        res.add(i * a + (n - 1 - i) * b)
    return sorted(list(res))


if __name__ == '__main__':

    T = int(input())
    l = []
    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)
        l.append(result)
    for guess in l:
        print(' '.join(map(str, guess)))

input('press enter to exit...')

