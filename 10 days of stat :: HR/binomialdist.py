
"""
Probability given odds:  odds / 1 + odds
Odds given probability: probability / 1- probability 
Here we are given that The ratio of boys to girls for babies born in Russia is 1.09:1.

That means the probability of it being a boy is given as 1.09 / 2.09

P(B) = 1.09/2.09
P(G) = 1 - (P(B))


"""

import math
import sys

# b = [float(i) for i in sys.stdin.readline().split()]

def nCx(n ,x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n-x))


n = 6
# pB = b[0] / b[0] + b[1]
pB = 1.09/2.09
pG = 1 - pB 
ans = 0

for i in range(3,n+1):
    ans += nCx(n, i)*(pB ** i)*(pG ** (n-i))


print(ans)