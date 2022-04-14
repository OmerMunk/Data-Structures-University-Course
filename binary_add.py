def binary_add(arr1, arr2):
    c = [-1]*(len(arr1)+1)
    carry = 0
    for i in range(len(arr1)-1, -1, -1):
        add = arr1[i] + arr2[i] + carry
        carry = 0
        if add >= 2:
            carry = 1
            add = add%2
        c[i+1] = add


    c[0] = carry
    print(c)


arr1= [1,0,1,0,1,0,1,0]
arr2= [1,1,0,0,1,1,0,0]
binary_add(arr1,arr2)

# 10101010 + 11001100
# = 0101110110
