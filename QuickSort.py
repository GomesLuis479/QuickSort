# An implementation of the randomised quick sort algorithm
# with average running time of O(nlogn).

import random


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def sorter(arr, start, end):

    if start >= end:
        return

    random_pos = random.randint(start, end)

    if random_pos != start:
        swap(arr, random_pos, start)

    pivot = arr[start]
    i = start
    for j in range(start+1, end+1):
        if arr[j] <= pivot:
            i = i + 1
            swap(arr, i, j)

    swap(arr, start, i)

    sorter(arr, start, i-1)
    sorter(arr, i+1, end)

    return


def quick_sort(arr):
    return sorter(arr, 0, len(arr)-1)


test_array = [60, 3, 5, 6, 100, 12, 8, 18, 45, 3, 13]
quick_sort(test_array)
print(test_array)


