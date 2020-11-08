# IEEE_Rookies_task_04_part_02
# name: Mahmoud_Ramadan
# task: insertion sort.


def insertion_sort(arr):
    for i in range(1, len(arr)):  # i =2
        key = arr[i]  # 3      # key = 2
        j = i - 1     # 0      # j = 1
        while j >= 0 and arr[j] > key: # 3 > 2
            arr[j+1] = arr[j]
            j = j - 1

        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    # this line is to if you want the user to enter the array himself.
    # arr = list(map(int, input('enter random numbers of an array: ').split()))
    arr = [22, 11, 3, 2, 1, 99, 66, 15, 48, 78, 42, 32,65, 15]
    print('array before sorting: ')
    print(arr)
    print('array after sorting: ')
    print(insertion_sort(arr))

input("press enter to exit....")






