def hype_print(hype_a, i ,j, to_print):
    if i >= len(hype_a):
        return
    to_print[j].append(hype_a[i])
    hype_print(hype_a, i*2, j+1, to_print )
    hype_print(hype_a, (i*2)+1, j+1, to_print )
    return to_print

heap = [0,16,4,10,14,7,9,3,2,8,1]

empty_arr = [[],[],[],[]]

print1 = hype_print(heap, 1, 0, empty_arr)
j = len(print1)*2
for i in range(len(print1)):
    print(" "*j, end=" ")
    print(print1[i], end=" ")
    print(" "*j, end=" ")
    print(" ")
    j = j-2