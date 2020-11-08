# IEEE_Rookies_task_03_part_02
# name: Mahmoud_Ramadan
# task: Write a program that takes a sentence and prints it, word per line, in a rectangular frame.

# getting the words from the user.
n = input('write random words!: ')


def frame_words(words):
    size = len(max(words, key=len))
    # print upper frame
    print('*'*(size + 4))
    # print mid frame
    for word in words:
        # formatting type: Use "<" to left-align the value:
        print('* {a:<{b}} *'.format(a=word, b=size))
    # printing lower frame
    print('*'*(size + 4))


print(frame_words(n.split(" ")))

# random words to use
# ahmed ali hassan ibrahimovitch salah jo

input("enter enter to exit...")