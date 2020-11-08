# IEEE_Rookies_task_25_part_01
# name: Mahmoud_Ramadan
# task: kaprekar number
# link: https://www.hackerrank.com/challenges/kaprekar-numbers/problem



#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    l = []
    for i in range(p, q + 1):
        sqr_i = i ** 2
        str_sqr_i = str(sqr_i)
        num_d = len(str_sqr_i) // 2

        if i == 1:
            l.append(i)
        elif len(str_sqr_i) > 1 and i == int(str_sqr_i[:num_d]) + int(str_sqr_i[num_d:]):
            l.append(i)

    if len(l) == 0:
        print("INVALID RANGE")
    else:
        print(' '.join(map(str, l)))


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
