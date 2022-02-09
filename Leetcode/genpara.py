# from itertools import combinations
import itertools as it

# make combinations
# print(list(it.combinations(('(',')'), 3)))

sstring =['(',')']
  
# size of combination is set to 3 
a = it.combinations(sstring, 3)  
y = [' '.join(i) for i in a] 
print(y)
  