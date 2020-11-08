# IEEE_Rookies_task_13_part_03
# name: Mahmoud_Ramadan
# task: sales by match
# link: https://www.hackerrank.com/challenges/sock-merchant/problem

'''
import math
import os
import random
import re
import sys
'''

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    c = 0
    dic = {}
    for i in ar:
        dic[i] = dic.get(i, 0) + 1

    for i in dic.keys():
        c += dic[i] // 2
    return c


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print('''you can use this as an input:
9
10 20 20 10 10 30 50 10 20
    ''')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(str(result))

    input('press enter to exit...')
    #fptr.write(str(result) + '\n')

    #fptr.close()
