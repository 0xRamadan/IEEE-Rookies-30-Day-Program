# IEEE_Rookies_task_06_part_01
# name: Mahmoud_Ramadan
# task: Draw Book
# link: https://www.hackerrank.com/challenges/drawing-book/problem


def pageCount(n, p):

    front_turn = p//2
    if n%2 == 1:
        back_turn = (n-p)//2
    else:
        back_turn = (n-p+1)//2
    return min(back_turn, front_turn)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print('''you can use this as an input:
6
5''')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)
    print(result)

    input('press enter to exit...')

    #fptr.write(str(result) + '\n')

    #fptr.close()
