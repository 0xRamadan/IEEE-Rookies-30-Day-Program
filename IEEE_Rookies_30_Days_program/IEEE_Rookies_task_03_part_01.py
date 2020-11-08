# IEEE_Rookies_task_03_part_01
# name: Mahmoud_Ramadan
# Implementing binary search.

# fill a list using list comprehension
data = [i for i in range(0, 51)]
# the target that the user want to search for in the list
target = 30


# binary search using loops.
def binary_search_iterative(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# binary search using recursion
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


print("Iterative binary search: ")
print(binary_search_iterative(data, target))
print("Recursive binary search: ")
print(binary_search_recursive(data, target, 0, len(data) - 1))

input("enter enter to exit...")