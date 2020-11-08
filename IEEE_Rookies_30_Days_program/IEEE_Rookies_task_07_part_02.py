# IEEE_Rookies_task_07_part_02
# name: Mahmoud_Ramadan
# task: diagonal difference.


def diagonalDifference(arr):
    # Write your code here
    primary_diagonal = []
    secondary_diagonal = []
    for i in range(n):
        primary_diagonal.append(arr[i][i])
        secondary_diagonal.append(arr[i][n - 1 - i])

    return abs(sum(primary_diagonal) - sum(secondary_diagonal))


if __name__ == '__main__':
    print('you can use this as an input: ')
    print('''3
11 2 4
4 5 6
10 8 -12''')
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
input('press enter to exit...')


