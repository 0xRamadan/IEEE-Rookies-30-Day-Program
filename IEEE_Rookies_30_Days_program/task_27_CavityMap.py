# IEEE_Rookies_task_27_part_02
# name: Mahmoud_Ramadan
# task: Cavity Map
# link: https://www.hackerrank.com/challenges/cavity-map/problem




import math
import os
import random
import re
import sys


def cavityMap(grid):
    l = [list(x) for x in grid]
    # output of this code:
    # 2-D Array
    '''
        [['1', '1', '1', '2'],
         ['1', '9', '1', '2'], 
         ['1', '8', '9', '2'],
         ['1', '2', '3', '4']]
    '''

    # iterate on 2-d array
    # start from row 1, column 1
    for i in range(1, n-1):
        for j in range(1, n-1):
            if l[i][j] > l[i-1][j] and l[i][j] > l[i+1][j] and l[i][j] > l[i][j-1] and l[i][j] > l[i][j +1]:
                l[i][j] = "X"

    return [''.join(x) for x in l]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
