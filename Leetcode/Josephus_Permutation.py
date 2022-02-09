


# list1 = [1,2,3,4,5,6]

n = 9

# print(len(list1))

# ans should be 0

def Josephus_Permutation(n, offset):
    offset -= 1
    idx = offset
    list1 = list(range(n))
    while len(list1) > 1:
        # kill
        print(list1.pop(idx))
        idx = (idx + offset) % len(list1)
    print('survivor',list1[0])


Josephus_Permutation(n, 2)
