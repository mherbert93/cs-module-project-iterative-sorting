def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    start = 0
    end = (len(arr) - 1)

    found = -1
    while end >= start and found == -1:
        middle_index = (start + end) // 2

        if arr[middle_index] == target:
            return middle_index
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1


    return -1  # not found
