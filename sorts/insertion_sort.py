def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key
    return arr


if __name__ == "__main__":
    l1 = [1,9,7,8,3,2]
    print(insertion_sort(l1))