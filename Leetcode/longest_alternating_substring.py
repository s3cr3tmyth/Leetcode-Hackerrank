#  Longest Alternating Substring

#  Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. 
#  If two or more substrings have the same length, return the substring that occurs first.


string1 = ("853667717122615664748443484823")


### use string slicing or enumerate


sol = ""

for idx, _ in enumerate(string1):
    # print(string1[idx])
    if (int(string1[idx-1]) % 2 != int(string1[idx]) % 2):
    # if x[::i] % 2 != x[::i+1] % 2:
        sol += string1[idx]
    else:
        sol += " " + string1[idx]

op = max(sol.split(" "), key=len)

# for multiple same length strings 
# op = [s for s in sol.split(" ") if len(s) == len(max(sol.split(" "), key=len))][0]

print(op)