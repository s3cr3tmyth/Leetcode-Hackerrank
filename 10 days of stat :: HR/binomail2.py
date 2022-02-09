import math

def nCx(n ,x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n-x))

n = 10
pB = 0.12
pG = 1 - pB 
ans = 0
ans2 = 0

for i in range(3):
    ans += nCx(n, i)*(pB ** i)*(pG ** (n-i))

for i in range(2,11):
    ans2 += nCx(n, i)*(pB ** i)*(pG ** (n-i))

print(round(ans,3))    
print(round(ans2,3))
