lst = [[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]

# if not lst:
L = sorted([len(i) for i in lst])
# start, end = L[0], L[-1]
M = sum(range(L[0],L[-1]+1)) - sum(L)
print(M)