# IEEE_Rookies_task_22
# name: Mahmoud_Ramadan
# task: Build Max Heap

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_down(arr, length, index):
    # start indexing from index zero
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index
    if length > left and arr[largest] < arr[left]:
        largest = left
    if length > right and arr[largest] < arr[right]:
        largest = right
    if largest != index:
        swap(arr, index, largest)
        bubble_down(arr , length, largest)


def buildHeap(arr, length):
    start_index = length // 2 - 1
    for i in range(start_index, -1, -1):
        bubble_down(arr, length, i)


def printHeap(arr, length):
    for i in range(length):
        print(arr[i], end=" ")


if __name__ == '__main__':
    print('''you can use this as input:
81 13 77 24 35 61 48 3 23 87 92 95 74 57 99 86 28 15 55 7 51''')
    arr = list(map(int, input().split()))

    length = len(arr)

    buildHeap(arr, length)

    printHeap(arr, length)