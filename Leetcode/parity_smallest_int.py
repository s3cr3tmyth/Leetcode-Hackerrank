L = [-31, -7, -13, -7, -9, -13]

min = L[0]

for i in L:
    if i < min:
        min = i

# x = [i for i, value in enumerate(L) if value == min])

x = list(filter(lambda x: L[x] == min, range(len(L))))


if int(min / 2) * 2 == min:
    print({"@index " + str(x[0]): min, "parity": "even"})
else:
    print({"@index " + str(x[0]): min, "parity": "odd"})