string = 'abcdefab'

set= {}
maximum = 0
start = 0

for i in range(len(string)):
    if string[i] in set:
        start = max(start, set[i]+1)
    set[string[i]] = i
    maximum = max(maximum, i-start+1)
