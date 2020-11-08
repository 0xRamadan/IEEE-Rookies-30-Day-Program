# IEEE_Rookies_task_01_part_01
# name: Mahmoud_Ramadan
# get the sum of a list using for loop, while loop and recursion.


# define a function to get the sum of a list using for loop.
def sum_for_loop(l):
    total = 0
    for i in range(len(l)):
        total += l[i]
    return print(total)


# define a function to get sum of a list using while loop.
def sum_while_loop(l):
    i = 0
    total = 0
    while i < len(l):
        total += l[i]
        i += 1
    return print(total)


# using recursion to get the sum of a list.
def sum_recur(l):
    if len(l) == 0:
        return 0

    return l[0] + sum_recur(l[1:])


if __name__ == "__main__":
    length = int(input())
    l = list(map(int, input().split()))
    sum_for_loop(l)
    sum_while_loop(l)
    print(sum_recur(l))
