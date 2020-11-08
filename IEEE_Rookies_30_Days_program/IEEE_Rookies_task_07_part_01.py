# IEEE_Rookies_task_07_part_01
# name: Mahmoud_Ramadan
# task: Write a program that takes a sorted list as an input and removes the duplicates.


# soution in one line of code.
# x = sorted(set(map(int,input("enter numbers: ").split())))

# taking a sorted list as an input.
x = sorted(list(map(int, input("enter numbers: ").split())))

# removing the duplicates.
x = set(x)
for i in x:
    print(i, end=' ')

input('\npress enter to exit...')