# IEEE_Rookies_task_12_part_01
# name: Mahmoud_Ramadan
# task: Number line jump


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 >= v1:
        return "NO"
    else:
        if (x2 - x1) % (v1 - v2) == 0:
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    print('''you can use this as an input:
0 3 4 2
''')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)

    input('press enter to exit...')
