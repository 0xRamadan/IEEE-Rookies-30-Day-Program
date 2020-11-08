# IEEE_Rookies_task_05_part_02
# name: Mahmoud_Ramadan
# task : Finding the percentage
print("re-enter these values of lines as input")
print("first line input: 2\nsecond line input:Harsh 25 26.5 28\nthird line input: Anurag 26 28 30\nfourth line input: Harsh")


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        scores = sum(scores) / len(scores)
        student_marks[name] = scores
    query_name = input()

    print('%.2f' % student_marks[query_name])


input('press enter to exit...')