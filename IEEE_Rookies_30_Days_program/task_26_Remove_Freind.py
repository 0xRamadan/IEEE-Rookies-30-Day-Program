# IEEE_Rookies_task_26_part_01
# name: Mahmoud_Ramadan
# task: Remove Friend
# link: https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/practice-problems/algorithm/remove-friends-5/submissions/


def delete(n, k, a):
    temp = []
    for i in a:
        while k and temp and temp[-1] < i:
            temp.pop()
            k -= 1
        temp.append(i)
    print(' '.join(map(str, temp)))


if __name__ == '__main__':
    for i in range(int(input())):

        n, k = map(int, input().split())

        friend = map(int, input().split())

        delete(n, k, friend)
