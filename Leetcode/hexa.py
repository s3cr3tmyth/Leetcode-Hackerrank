color = "#00FF00"

r = int(color[1:3], 16)
g = int(color[3:5], 16)
b = int(color[5:7], 16)

# print(r,g,b)

rgb = [255,155,000]

# for i in rgb:
r = [format(i, '02x') for i in rgb]


print(r)

