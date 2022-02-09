# Rearrange the barcodes so that no two adjacent barcodes are equal.  
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]



import collections
packages = [1,1,1,1,2,2,3,3]
i, n = 0, len(packages)
res = [0] * n
# print(res)
for k, v in collections.Counter(packages).most_common():
    for _ in range(v):
        res[i] = k
        # print(res)
        i += 2
        if i >= n: i = 1
