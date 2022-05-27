def swap(arr1, index1, index2):
    temp = arr1[index1]
    arr1[index1] = arr1[index2]
    arr1[index2] = temp


def selection_sort(arr1):
    for i in range (0, len(arr1)-1):
        minIndex = i
        for j in range(i, len(arr1)):
             if arr1[j] < arr1[minIndex]:
                 minIndex = j
        swap(arr1, i, minIndex)



if __name__ == "__main__":
    array = [1,3,2,5,7,4,9,8,12,0,32,-4,20,15]
    selection_sort(array)
    print(array)

