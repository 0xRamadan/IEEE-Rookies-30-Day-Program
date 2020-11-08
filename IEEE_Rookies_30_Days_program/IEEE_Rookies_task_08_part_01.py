# IEEE_Rookies_task_08_part_01
# name: Mahmoud_Ramadan
# task: gintroS problem on HackerRank.

import re
if __name__ == '__main__':
    txt = input('you can enter this as an input < Sorting1234 > : ').rstrip()
    x = re.findall("[a-z]", txt)
    low = sorted(x)

    u = re.findall("[A-Z]", txt)
    upp = sorted(u)

    n = re.findall("[0-9]", txt)
    con = list(map(int, sorted(n)))

    od = []
    ev = []
    for i in range(len(con)):
        if con[i]%2 != 0:
            od.append(con[i])
        elif con[i]%2 == 0:
            ev.append(con[i])

    low.extend(upp)
    low.extend(od)
    low.extend(ev)
    low =list(map(str,low))
    print("".join(low))

input('press enter to exit...')
