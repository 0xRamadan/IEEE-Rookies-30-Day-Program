# IEEE_Rookies_task_29
# name: Mahmoud_Ramadan
# task: hackerrank in a string
# link: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

import math
import os
import random
import re
import sys


# Complete the hackerrankInString function below.
def hackerrankInString(s):
    # s = list('h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k')
    n = 'hackerrank'
    l = len(n)
    i = 0
    for c in s:
        if c == n[i]:
            i += 1
            if i == l:
                return 'YES'
    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        #fptr.write(result + '\n')
        print(result)

    #fptr.close()
