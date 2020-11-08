# IEEE_Rookies_task_05_part_01
# name: Mahmoud_Ramadan
# task: bubble sort


def bubble_sort(arr):                # index    0  1  2  3  4  5  6
    for i in range(len(arr)-1, 1, -1): # arr = [3, 2, 6, 5, 4, 9, 8]
        for j in range(i):             #        2  3  5  4  6  8  9 # first iteration
            if arr[j] > arr[j+1]:      # ----------------------
                temp = arr[j]          #
                arr[j] = arr[j+1]      # swap
                arr[j+1] = temp        # ----------------------
    return arr

arr = [3, 2, 6, 5, 4, 9, 8]
print("list before using bubble sort: ")
print(arr)
print("list after using bubble sort: ")
print(bubble_sort(arr))

input('press enter to exit...')

