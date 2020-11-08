# IEEE_Rookies_task_12_part_01
# name: Mahmoud_Ramadan
# task: Bob and String
# link: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/bob-and-string-easy/submissions/


def countOperation(S1, S2):

    count1 = [0] * 26
    count2 = [0] * 26

    i = 0
    while i < len(S1):
        count1[ord(S1[i]) - ord('a')] += 1
        i += 1

    i = 0
    while i < len(S2):
        count2[ord(S2[i]) - ord('a')] += 1
        i += 1

    count = 0
    for i in range(26):
        count += abs(count1[i] - count2[i])
    return count


if __name__ == "__main__":
    num_testCase = int(input())

    l = []
    for _ in range(2 * num_testCase):
        l.append(input())

    i = 0
    while i < (2 * num_testCase):
        print(countOperation(l[i], l[i+1]))
        i += 2