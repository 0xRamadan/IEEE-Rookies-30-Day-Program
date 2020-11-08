# IEEE_Rookies_task_01_part_01
# name: Mahmoud_Ramadan
# printing prime numbers


# first, checking if the number is a prime number.
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# second, printing prime numbers.
def printPrime(n):
    for i in range(n + 1):
        if isPrime(i):
            print(i, end=' ')


if __name__ == "__main__":
    n = int(input('enter a number where number > 1: '))
    printPrime(n)
