# IEEE_Rookies_task_04_part_02
# name: Mahmoud_Ramadan
# task: find the runner-up score.


"""if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

x = sorted(list(arr))
a = x[-1]
for i in range(len(x)):
    if x[i] == a:
        print(x[i-1])
        break
"""
# another solution
if __name__ == '__main__':
    n = int(input('number of runners: '))
    arr = list(map(int, input("enter scores: ").split()))
m = max(arr)
c = arr.count(m)
for i in range(c):
    arr.remove(m)
print(max(arr))

input("press enter to exit...")
