import math

# all functions assume first index of heap is 1

class heap_functions:

    @staticmethod
    def parent(i):
        return math.floor(i/2)

    @staticmethod
    def left(i):
        return 2*i

    @staticmethod
    def right(i):
        return 2*i+1


    @staticmethod
    def max_heapify(heap, i):
        left = heap_functions.left(i)
        right = heap_functions.right(i)
        if left <= len(heap) and heap[left] > heap[i]:
            largest = left
        else:
            largest = i
        if right <= len(heap) and heap[right] > heap[largest]:
            largest = right
        if largest != i:
            temp = heap[i]
            heap[i] = heap[largest]
            heap[largest] = temp
            heap_functions.max_heapify(heap, largest)

    @staticmethod
    def heap_print_order(hype_a, i, j, to_print):
        if i >= len(hype_a):
            return
        to_print[j].append(hype_a[i])
        heap_functions.heap_print_order(hype_a, i * 2, j + 1, to_print)
        heap_functions.heap_print_order(hype_a, (i * 2) + 1, j + 1, to_print)
        return to_print

    @staticmethod
    def heap_printer(heap_ordered):
        j = len(heap_ordered) * 2
        for i in range(len(heap_ordered)):
            print(" " * j, end=" ")
            print(heap_ordered[i], end=" ")
            print(" " * j, end=" ")
            print(" ")
            j = j - 2

