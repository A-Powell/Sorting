# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = []

    a, b = 0, 0  # starting at beginning of `a` and `b`

    while a < len(arrA) and b < len(arrB):
        # compare the next value of each
        # add smallest to `merged_arr`
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1
    # add extra elements (if any)
    if a == len(arrA):
        merged_arr.extend(arrB[b:])
    else:
        merged_arr.extend(arrA[a:])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        mid = int(len(arr)//2)
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        arr = merge(left, right)

    return arr


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
