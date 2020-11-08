# IEEE_Rookies_task_15
# name: Mahmoud_Ramadan
# task: Climbing the leaderboard
# link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


def climbingLeaderboard(ranked, player):
    # Write your code here

    ranked = list(set(ranked))
    ranked.sort()
    n = len(ranked)
    count = 0
    result = []
    for k in player:
        while count < n and ranked[count] <= k:
            count += 1
        result.append(n - count + 1)

    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print('''you can use this as an input:
7
100 100 50 40 40 20 10
4
5 25 50 120''')


    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))

    input('press enter to exit...')
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
