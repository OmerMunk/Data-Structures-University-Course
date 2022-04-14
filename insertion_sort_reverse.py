def insertion_sort_descending(arr):
    for j in range(len(arr)-2, -1, -1):
        key = arr[j]
        i = j+1
        while i < len(arr) and arr[i] > key:
            arr[i-1] = arr[i]
            i = i+1
        arr[i-1] = key
    return arr


if __name__ == "__main__":
    l1 = [1,9,7,8,3,2]
    print(insertion_sort_descending(l1))