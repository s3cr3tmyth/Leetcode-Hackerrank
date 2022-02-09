l1 = [6, 12, 8, 10, 20, 16]
l2 = [5, 4, 3, 2, 1, 5]


l3 = [y for i, (_,_) in enumerate(zip(l1,l2)) for y in [l1[i]] * l2[i]]


def median(arr):
    if len(arr) % 2 == 0:
        return sum(arr[len(arr)//2-1:len(arr)//2+1])/2
    else:
        return arr[len(arr)//2]


def quartiles_range(l):
    q1 = median(l[:len(l)//2])
    q2 = median(l)
    if len(l) % 2 == 0:
        q3 = median(l[len(l)//2:]) 
    else:
        q3 = median(l[len(l)//2+1:]) 
    
    return (q3-q1)


print(quartiles_range(l3))