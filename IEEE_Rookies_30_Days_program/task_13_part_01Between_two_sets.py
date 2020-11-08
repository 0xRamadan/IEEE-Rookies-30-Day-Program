# IEEE_Rookies_task_04_part_02
# name: Mahmoud_Ramadan
# task: Between two sets
# link: https://www.hackerrank.com/challenges/between-two-sets/problem

'''
import math
import os
import random
import re
import sys
'''


def getTotalX(a, b):
    a_fact = []
    b_fact = []
    common_fact = []
    # number of modules operation for a number to make sure that the number is a factor for each arrays
    num_of_mod = len(a + b)
    for i in range(max(a), min(b) + 1, max(a)):
        for num in a:
            if i % num == 0:
                a_fact.append(i)
        for num in b:
            if num % i == 0:
                b_fact.append(i)

    combine_fact = a_fact + b_fact
    for common in combine_fact:
        if combine_fact.count(common) == num_of_mod:
            common_fact.append(common)

    return len(set(common_fact))  # Write your code hre


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print('''you can use this as an input:
2 3
2 4
16 32 96''')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

    input('press enter to exit...')


"""fptr.write(str(total) + '\n')

fptr.close()"""
