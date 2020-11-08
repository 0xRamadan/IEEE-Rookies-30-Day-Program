# IEEE_Rookies_task_12_part_01
# name: Mahmoud_Ramadan
# task: Breaking the Records

# !/bin/python3
"""
import math
import os
import random
import re
import sys
"""

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest_scores = [scores[0]]
    lowest_scores = [scores[0]]
    counter1 = 0
    counter2 = 0
    for i in range(n):
        if scores[i] > highest_scores[-1]:
            highest_scores.append(scores[i])
            counter1 += 1
        else:
            highest_scores.append(highest_scores[-1])

        if scores[i] < lowest_scores[-1]:
            lowest_scores.append(scores[i])
            counter2 += 1
        else:
            lowest_scores.append(lowest_scores[-1])
    return [counter1, counter2]


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print('''you can use this as an input:
10
3 4 21 36 10 28 35 5 24 42''')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))

    input('press enter to exit...')


    '''fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()'''
