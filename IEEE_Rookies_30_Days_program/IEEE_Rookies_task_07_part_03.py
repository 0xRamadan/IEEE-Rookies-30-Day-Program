# IEEE_Rookies_task_07_part_03
# name: Mahmoud_Ramadan
# task: Python zip() function on hackerrank.
print("you can use this as an input: ")
print('''5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5''')

if __name__ == '__main__':
    data = list(map(int, input().split()))
    subjects = []
    for _ in range(data[1]):
        subjects.append(list(map(float, input().split())))
    for student_marks in zip(*subjects):
        print(sum(student_marks) / len(student_marks))

input('press enter to exit...')