# IEEE_Rookies_task_19_part_03
# name: Mahmoud_Ramadan
# task: beautiful Triplets
# link: https://www.hackerrank.com/challenges/beautiful-triplets/problem


'''
import math
import os
import random
import re
import sys'''

from collections import Counter


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    obj = Counter(arr)
    # objcet here, return dictionary with values = elements and keys = no. of each element
    count = 0
    for elem in arr:
        if obj[elem + d] and obj[elem + d + d]:
            count += 1
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(str(result))

    input('press enter to exit...')

    # fptr.write(str(result) + '\n')

    # fptr.close()
