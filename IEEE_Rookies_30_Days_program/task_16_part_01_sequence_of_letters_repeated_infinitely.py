# IEEE_Rookies_task_16_part_01
# name: Mahmoud_Ramadan
# task: sequence of letters repeated infinitely

import re


def repeat_string(sequence, length):

    number_of_repeats = length // len(sequence) + 1

    string_repeated = sequence * number_of_repeats

    string_repeated_to_n = string_repeated[:n]

    return string_repeated_to_n


if __name__ == '__main__':
    print('''you can use this as an input:
rar
10''')
    seq = input().strip()

    n = int(input())

    r = repeat_string(seq, n)
    print(r)

    find_r = re.findall('r', r)

    print(len(find_r))

    input('press enter to exit...')
