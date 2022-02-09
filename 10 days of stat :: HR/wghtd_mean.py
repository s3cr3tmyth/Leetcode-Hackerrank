x = [10, 40, 30, 50, 20]
w = [1, 2, 3, 4, 5]


x = round(sum([i*j for i,j in zip(x,w)])/sum(w),1)

print(x)