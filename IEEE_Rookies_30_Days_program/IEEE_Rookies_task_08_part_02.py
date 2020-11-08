# IEEE_Rookies_task_08_part_01
# name: Mahmoud_Ramadan
# task: guessing program hit or miss.


'''
import random
rand = random.randint(100, 1000)
rand = str(rand)
count = 0
while True:
    hit = 0
    miss = 0
    guess = int(input("Enter a 3-digit number: "))
    if guess >= 1000 or guess <= 99:
        print('please enter a 3-digit number next time.')
        continue
    for i in str(guess):
        if i in rand:
            if str(guess).index(i) == rand.index(i):
                hit += 1
            else:
                miss += 1
    count += 1
    if hit >= 3:
        hit = 3
        miss = 0
        print("{0} hit {1} miss".format(hit, miss))
        break
    else:
        print("{0} hit {1} miss".format(hit, miss))

print("number of Attempts is ", count)
'''


# better solution
import random


def getDifferences(a, b):
    return [index for index, elem in enumerate(b) if elem != a[index]]


l = [random.randint(0, 9) for i in range(3)]
print("Enter a 3-digit number: ")
numberOfAttempts = 0
while 1:
    x = list(map(int, input()))
    if len(x) != 3:
        print('please you have to enter a 3-digit number next time. ')
        print("Enter a 3-digit number: ")
        continue
    numberOfAttempts += 1
    res = getDifferences(x, l)
    if len(res) == 0:
        print("hit: 3")
        break
    else:
        print("hit: ", len(l) - len(res))
        print("miss: ", len(res))

print("It takes you: " + str(numberOfAttempts) +
      " attempt to guess the correct answer.")


input("press enter to exit...")
