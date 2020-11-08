# IEEE_Rookies_task_02_part_01
# name: Mahmoud_Ramadan
# number guessing game

import random as rand
r = rand.randrange(1, 11)
k = int(input("Enter an integer number between 1 and 10. "))
count = 1
while True:
    if k == r:
        print(count)
        break

    elif k != r:
        new_k = int(input('Wrong! try again. '))
        count += 1
        k = new_k
print("\n")
input("enter to exit...")


