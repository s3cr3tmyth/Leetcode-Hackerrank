
import math

# n = int(input())
# X = [float(x) for x in input().split()]
# Y = [float(x) for x in input().split()]

# X = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
# Y = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]


def sd(ll):
    mean = sum(ll) / len(ll)
    sqdiff = sum([(i - mean)**2 for i in ll])
    var = sqdiff / len(ll)
    return math.sqrt(var)

def corr(x,y):
    meanx = sum(x) / len(x)
    meany = sum(y) / len(y)
    res = 0
    for i in range(len(x)):
        res += (x[i] - meanx)* (y[i] - meany)
    return res/(len(x)*sd(x)*sd(y))


print(round(corr(X,Y),3))