# IEEE_Rookies_task_12_Bonus
# name: Mahmoud_Ramadan
# task: perform a specific routine on a given number.


def asc_sort(result):
    s = list(sorted(str(result)))[::-1]
    return int(''.join(s))


def desc_sort(result):
    l = list(sorted(str(result)))
    return int(''.join(l))


result = int(input())
counter = 0
while result != 6174:
    # making sure that the number is always 4 digits
    # putting the while statement here in case if the given number
    # has less than four digits
    while len(str(result)) < 4:
        result = str(result) + '0'

    asc_num = asc_sort(result)
    desc_num = desc_sort(result)

    counter += 1
    result = asc_num - desc_num


print(counter)

input('press enter to exit...')
