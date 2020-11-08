# IEEE_Rookies_task_07_part_02
# name: Mahmoud_Ramadan
# task: find Digits
# link: https://www.hackerrank.com/challenges/find-digits/problem


import math
import os
import random
import re
import sys


# Complete the findDigits function below.
def findDigits(n):
    d = 0
    s = str(n)
    for i in range(len(s)):
        if int(s[i]) == 0:
            print(ZeroDivisionError)
        else:
            if n % int(s[i]) == 0:
                d += 1
    return d


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

