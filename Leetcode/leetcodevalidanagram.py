s = 'abcdef'
t = 'asdsds'

# for i in range(len(s)):
#     for j in range(len(t)):
if sorted(i) == sorted(j):
    return True
else:
    return False


##### other fastest solution
return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])