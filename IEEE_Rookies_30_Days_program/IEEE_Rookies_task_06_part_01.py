# IEEE_Rookies_task_06_part_01
# name: Mahmoud_Ramadan
# task: nested list


marksheet = []
scoresheet = []
print('you can use this as an input: ')
print('5\nHarry\n37.21\nBerry\n37.21\nTina\n37.2\nAkriti\n41\nHarsh\n39\n')
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet += [[name, score]]  # nested list
        scoresheet += [score]

    # to make sure getting the second lowest grades  # {1, 2, 3, 4, 5} second lowest is 2
    second_lowest = sorted(set(scoresheet))[1]

    # iterate using for loop
    for student_name, grade in sorted(marksheet):
        if grade == second_lowest:
            print(student_name)

input('press enter to exit...')