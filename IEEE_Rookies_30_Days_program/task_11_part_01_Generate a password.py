# IEEE_Rookies_task_11_part_01
# name: Mahmoud_Ramadan
# task: Generate a password

import random
import string


def generate_password(size):
    l = [random.choice(string.ascii_lowercase +
                              string.ascii_uppercase +
                              string.digits +
                              '@#$%')for n in range(size)]
    gen_pass = ''.join(l)
    return gen_pass

password = generate_password(10)
print(password)

input('press enter to exit...')
