import sys


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


if __name__ == "__main__":
    array1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    mergedArray = merge(array1, 0, 4, 9)
    print(mergedArray)
