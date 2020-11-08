# IEEE_Rookies_task_23
# name: Mahmoud_Ramadan
# task: ACM_ICPC Team HackerRank
# link: https://www.hackerrank.com/challenges/acm-icpc-team/problem

import math
import os
import random
import re
import sys


# Complete the acmTeam function below.
def acmTeam(topic):
    max_topic = 0
    num_teams = 0
    for i in range(n):
        for j in range(i, n):
            __topic = 0
            for x, y in zip(topic[i], topic[j]):
                if x == '1' or y == '1':
                    __topic += 1
            if __topic > max_topic:
                max_topic = __topic
                num_teams = 1
            elif __topic == max_topic:
                num_teams += 1

    return [max_topic, num_teams]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
