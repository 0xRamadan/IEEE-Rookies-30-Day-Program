# IEEE_Rookies_task_09_part_01
# name: Mahmoud_Ramadan
# task: check the validity of a password

import re

# p= input("Input your password: ")
n = int(input("enter number of test cases: "))
password = []
for i in range(n):
    password.append(input())
for p in password:
    x = True
    while x:
        if len(p) < 6 or len(p) > 20:
            break
        elif not re.search("[a-z]", p):
            break
        elif not re.search("[0-9]", p):
            break
        elif not re.search("[A-Z]", p):
            break
        elif not re.search("[$#@]", p):
            break
        elif re.search("\s", p):  # return a match if the string contain a white space.
            break
        else:
            print("Valid Password")
            x = False
            break

    if x:
        print("Not a Valid Password")


input("press enter to exit....")

