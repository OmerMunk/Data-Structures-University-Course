def linear_search( arr, target):
    i = 0
    while i < len(arr) and arr[i] != target:
        i = i+1
    if i >= len(arr):
        return None
    return i


def sorted_linear_search( arr, target): # assuming that that array is  ascending or at least not descending
    i = -1
    while i< len(arr)-1:
        i = i+1
        if arr[i] == target:
            return i
        if arr[i] > target:
            return None


def sorted_linear_search_from_right( arr, target): # assuming that that array is  ascending or at least not descending
    i = len(arr)
    while i > 0:
        i = i-1
        if arr[i] == target:
            return i
        if arr[i] < target:
            return None

if __name__ == "__main__":
    # l1 = [1,23,44,67,87,98,123,45,6]
    # print(linear_search(l1, 0))
    l2= [10,20,30,40,50,60,70,80]
    print(sorted_linear_search_from_right(l2, 200))
