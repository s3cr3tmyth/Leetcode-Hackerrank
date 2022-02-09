# Given an array with numerical values, write a function to provide 
# the multiply results of all other elements except the current one in the array. 
# e.g: [1,2,3,4] gives you [24, 12, 8, 6].

import numpy as np

ll = [1,2,3,4]

ans = [int((np.prod(np.array((ll))) / j)) for j in ll]

print(ans)
