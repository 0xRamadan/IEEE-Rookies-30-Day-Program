# IEEE_Rookies_task_05_part_02
# name: Mahmoud_Ramadan
# task: Any or All - python built-in functions

# solution in three lines of code.
if __name__ == '__main__':
    n = int(input('size of the list: '))
    arr = list(map(int, input("enter the numbers of the list: ").split()))

print(all(x > 0 for x in arr) and any(str(x) == str(x)[::-1] for x in arr))

input('press enter to exit...')

