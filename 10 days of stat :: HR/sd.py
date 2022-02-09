import math

N = 5

l1 = [10, 40, 30, 50, 20]

mean = sum(l1)/N

dev = math.sqrt(sum([(i-mean)**2 for i in l1])/N)

print(round(float(dev),1))