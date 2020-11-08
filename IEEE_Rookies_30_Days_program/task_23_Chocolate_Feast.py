# IEEE_Rookies_task_23
# name: Mahmoud_Ramadan
# task: Chocolate Feast
# link: https://www.hackerrank.com/challenges/chocolate-feast/problem


import math
import os
import random
import re
import sys


# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    bar = n // c
    wrappers = bar
    while wrappers >= m:
        bar += wrappers // m
        wrappers = wrappers // m + wrappers % m

    return bar


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
