sample = ['a','a','a','b','b','c']

from collections import Counter

z = Counter(sample)
ans = []
for k,v in z.items():
    ans.extend([str(k),str(v)])


print(ans)