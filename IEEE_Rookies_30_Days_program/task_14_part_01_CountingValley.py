# IEEE_Rookies_task_06_part_01
# name: Mahmoud_Ramadan
# task: Counting Valley
# link: https://www.hackerrank.com/challenges/counting-valleys/problem

'''
import math
import os
import random
import re
import sys
'''

def countingValleys(steps, path):
    countvalley = 0
    sealevel = 0
    for i in range(steps):
        if path[i] =='U':
            sealevel += 1
            if sealevel == 0:
                countvalley += 1
        else:
            sealevel -= 1
    return countvalley


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print('''you can use this as an input:
8
UDDDUDUU
''')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)

    input('press enter to exit...')

    #fptr.write(str(result) + '\n')

    #fptr.close()
