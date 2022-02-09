import math

# X = [95, 85, 80, 70, 60]
# Y = [85, 95, 70, 65, 70]

X = []; Y = []
for i in range(5):
    a,b=input().split()
    X.append(int(a))
    Y.append(int(b)) 

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

# find bias b
b = (corr(X,Y) * sd(Y)) / sd(X)
# find coeffecint a
a = (sum(Y) / len(Y)) - b * (sum(X) / len(X))
# ans = a + bX
y = a + 80*b
print(round(y,3))

