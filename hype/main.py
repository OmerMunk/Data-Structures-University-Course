from heap_functions import *


if __name__ == "__main__":
    heap = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    empty_arr = [[], [], [], []]

    ordered = heap_functions.heap_print_order(heap, 1, 0, empty_arr)
    heap_functions.heap_printer(ordered)
    heap_functions.max_heapify(heap, 2)
    empty_arr = [[], [], [], []]

    ordered = heap_functions.heap_print_order(heap, 1, 0, empty_arr)
    heap_functions.heap_printer(ordered)