
list1 = ([
  [1, 2, 4.4, "f", "a", "b"],
  [0], 
  [0.5, "d","X",3,"s"],
  ["f", "e", 8],
  ["p","Y","Z"],
  [12,18]
])
import functools
import operator

# sort the list

li = functools.reduce(operator.iconcat, list1, [])
li.sort(key = lambda i: ({int:0, float:0,str:1}.get(type(i), 0), i))

# set a counter
c = 0

for i, x in enumerate(list1):
    for j, a in enumerate(x): 
        list1[i][j] = li[c]
        c+=1
        

print(list1)


