# IEEE_Rookies_task_06_part_01
# name: Mahmoud_Ramadan
# task: Electronics Shop
# link: https://www.hackerrank.com/challenges/electronics-shop/problem


def getMoneySpent(keyboards, drives, b):
    tot_prop = []
    for i in keyboards:
        for j in drives:
            tot_prop.append(i+j)
    fine_prop = [x for x in tot_prop if x <= b]
    if not fine_prop:
        return -1
    else:
        return max(fine_prop)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print('''you can use this as an input:
10 2 3
3 1
5 2 8''')
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(str(moneySpent))
    input('press enter to exit...')
    #fptr.write(str(moneySpent) + '\n')

    #fptr.close()
