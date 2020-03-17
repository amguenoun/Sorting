# TO-DO: Complete the selection_sort() function below
import random


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        temp_holder = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp_holder

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while True:
        swap = False

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp_holder = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp_holder
                swap = True

        if not swap:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    if len(arr) in (0, 1):
        return arr

    for i in range(len(arr)):
        if maximum < arr[i]:
            maximum = arr[i]
        elif arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"

    counts = [0] * (maximum + 1)
    newArr = [0] * len(arr)

    # Store the count of each unique number in arr
    for i in range(len(arr)):
        counts[arr[i]] += 1

    # Modify count array to store the sum of previous counts
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i-1]

    for i in range(len(arr)):
        newArr[counts[arr[i]] - 1] = arr[i]
        counts[arr[i]] -= 1

    return newArr
