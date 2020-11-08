# IEEE_Rookies_task_06_part_01
# name: Mahmoud_Ramadan
# task: find a string

def count_substring(string, sub_string):
    c = 0
    str_len = len(string)
    sub_len = len(sub_string)
    for i in range(str_len - sub_len + 1):
        if (string[i:(i + len(sub_string))] == sub_string):
            c = c + 1
    return c


if __name__ == '__main__':
    string = input("enter a string: ").strip()
    sub_string = input("enter a substring: ").strip()

    count = count_substring(string, sub_string)
    print(count)

input('press enter to exit...')
