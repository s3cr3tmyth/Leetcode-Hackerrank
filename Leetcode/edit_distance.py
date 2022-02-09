# we build up solutions from smaller subproblems to bigger subproblems (bottom-up). 
# Initialize our 2D table with base constraints. 
# The first row and column of the table has known values since if one string is empty, 
# we simply add the length of the non-empty string since that is the minimum number of edits necessary. 
# the runtime is O(mn)
# the space complexity is O(mn) where m and n are the lengths of words


word1 = "intention"
word2 = "execution"
m = len(word1)
n = len(word2)
table = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(m + 1):
    table[i][0] = i
for j in range(n + 1):
    table[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
            table[i][j] = table[i - 1][j - 1]
        else:
            table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
            ##### add 1 for the operation
    
print(table[-1][-1])
