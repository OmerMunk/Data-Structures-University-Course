import math
import sys

# merge method with sentries
def merge(arr, p, q, r):  # Assuming that arr[p...q] is sorted and arr[q+1...r] is sorted
    n1 = q - p + 1  # length of the first sorted part of the array
    n2 = r - q  # length of the second pre-sorted part of the array
    L1 = [None] * (n1 + 1)
    L2 = [None] * (n2 + 1)
    for i in range(0, n1):
        L1[i] = arr[p + i]
    for i in range(0, n2):
        L2[i] = arr[q + 1 + i]
    L1[n1] = sys.maxsize
    L2[n2] = sys.maxsize
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L1[i] >= L2[j]:
            arr[k] = L2[j]
            j += 1
        else:
            arr[k] = L1[i]
            i += 1
    return arr

# merge method without sentries
def merge2(arr, p, q, r):  # Assuming that arr[p...q] is sorted and arr[q+1...r] is sorted
    n1 = q - p + 1  # length of the first sorted part of the array
    n2 = r - q  # length of the second pre-sorted part of the array
    L1 = [None] * (n1)
    L2 = [None] * (n2)
    for i in range(0, n1):
        L1[i] = arr[p + i]
    for i in range(0, n2):
        L2[i] = arr[q + 1 + i]
    i = 0
    j = 0
    k = p
    while k < r+1:
        while i < n1 and j < n2:
            if L1[i] >= L2[j]:
                arr[k] = L2[j]
                j += 1
            else:
                arr[k] = L1[i]
                i += 1
            k+=1
        if i == n2:
            for h in range(j, n2):
                arr[k] = L2[h]
                k+=1
        else:
            for h in range(i, n1):
                arr[k] = L1[h]
                k+=1

    return arr


def merge_sort(array, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)



if __name__ == "__main__":
    array1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    mergedArray = merge(array1, 0, 4, 9)
    print(mergedArray)

    array2 = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 98, 12, 87, 34, 65, 45]
    merge_sort(array2, 0, len(array2)-1)
    print(array2)
