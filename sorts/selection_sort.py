import sys


def swap(arr1, index1, index2):
    temp = arr1[index1]
    arr1[index1] = arr1[index2]
    arr1[index2] = temp


def selection_sort(arr1):
    for i in range(0, len(arr1) - 1):
        minIndex = i
        for j in range(i+1, len(arr1)):
            if arr1[j] < arr1[minIndex]:
                minIndex = j
        swap(arr1, i, minIndex)


def selection_sort_second_array(arr1):
    arr2 = [None] * len(arr1)
    for i in range(0, len(arr1)):
        minIndex = i
        for j in range(0, len(arr1)):
            if arr1[j] < arr1[minIndex]:
                minIndex = j
        arr2[i] = arr1[minIndex]
        arr1[minIndex] = sys.maxsize
    return arr2


if __name__ == "__main__":
    array_a = [1, 3, 2, 5, 7, 4, 9, 8, 12, 0, 32, -4, 20, 15]
    array_b = [8, 6, 9, 4, 3, 3, 2, 4, 5, 12, 13, 34, 32, 12]

    selection_sort(array_a)
    print(array_a)

    result = selection_sort_second_array(array_b)
    print(result)
