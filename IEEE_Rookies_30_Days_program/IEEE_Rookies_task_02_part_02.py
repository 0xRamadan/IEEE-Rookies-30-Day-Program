# IEEE_Rookies_task_02_part_02
# name: Mahmoud_Ramadan
# Fibonacci sequence task


# Fibonacci sequence task using recursion
def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    n = int(input('enter a number where number > 1: '))
    for i in range(n):
        print(fibonacci(i), end=' ')


"""
first, second = 0, 1
count = 0
if __name__ == '__main__':
    n = int(input('enter a number where number > 1: '))
    if n == 0:
        print(n)
    elif n == 1:
        print(n)
    else:
        while count < n:
            print(first, end=' ')
            next_num = first + second
            # fib sequence
            first = second
            second = next_num
            count += 1

"""
print("\n")
input("enter to exit...")

