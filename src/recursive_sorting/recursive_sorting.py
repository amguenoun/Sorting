# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    count, i, j = 0, 0, 0
    # compared left and right parts of array and assigns them to merged
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[count] = arrA[i]
            i += 1
        else:
            merged_arr[count] = arrB[j]
            j += 1
        count += 1

    # put the remained in merged, left first
    while i < len(arrA):
        merged_arr[count] = arrA[i]
        i += 1
        count += 1
    while j < len(arrB):
        merged_arr[count] = arrB[j]
        j += 1
        count += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        return merge(merge_sort(left), merge_sort(right))


# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
