# IEEE_Rookies_task_13_part_02
# name: Mahmoud_Ramadan
# task: Migratory Birds
# link: https://www.hackerrank.com/challenges/migratory-birds/problem
"""
import math
import os
import random
import re
import sys
"""


def migratoryBirds(arr):
    type_of_birds = [0]* len(arr)
    for i in range(len(arr)):
        # since there are only 5 types
        # so we are sure that any element inside arr can't be greater than 5
        type_of_birds[arr[i]] += 1
    # here the index() method, it returns the index of the first accurance of the given value
    # that means it will return the lowest id number of birds  if two or more types of birds were equally common
    return type_of_birds.index(max(type_of_birds))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print("""you can use this as an input:
11
1 2 3 4 5 4 3 2 1 3 4""")

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

    input('press enter to exit...')
    # fptr.write(str(result) + '\n')

    # fptr.close()
