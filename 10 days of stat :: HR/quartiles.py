

# N = int(input())
# x = list(map(int, input().split()))
# w = list(map(int, input().split()))

l = [3, 7, 8, 5, 14, 21, 13, 18]

def median(arr):
    if len(arr) % 2 == 0:
        # return int(arr[len(arr)/2] + arr[len(arr)/2+1])
        return sum(arr[len(arr)//2-1:len(arr)//2+1])/2
    else:
        return arr[len(arr)//2]


def quartiles(l):
    q1 = median(l[:len(l)//2])
    q2 = median(l)
    if len(l) % 2 == 0:
        q3 = median(l[len(l)//2:]) 
    else:
        q3 = median(l[len(l)//2+1:]) 
    
    return q1,q2,q3


q1,q2,q3 = quartiles(l)

print(q1,'\n',q2,'\n',q3)