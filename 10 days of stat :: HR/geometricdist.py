# n = 5
# pB = 1/3
# pG = 1 - pB 
# ans = (pG**(n-1)) * pB

# print(round(ans,3))


# II)
# p1 + p2 + p3+ p4 + p5
n = 5
pB = 1/3
pG = 1 - pB 
ans = sum([pG**(5-x)*pB for x in range(1,6)])
print(round(ans,3))
