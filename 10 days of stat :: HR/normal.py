# import math
# mu = 20
# sd = 2
# x = 19.5
# y1 = 20
# y2 = 22


# cdf = lambda x: 0.5 * (1 + math.erf((x - mu) / (sd * (2 ** 0.5))))

# ans = cdf(x)
# ans2 = cdf(y1)
# ans3 = cdf(y2)
# ans4 = ans3 - ans2
# print(round(ans,3))
# print(round(ans4,3))


### 2nd prob

import math
mu, sd = 70, 10
x = 80
y = 60
z = 60


cdf = lambda x: 0.5 * (1 + math.erf((x - mu) / (sd * (2 ** 0.5))))

### greater than 80 meaning 1 - less than 80
ans = (1 - cdf(x)) * 100
### greater than equal to 60 meaning 1 - less than equal to 60
ans2 = (1 - cdf(y)) * 100
### same as prev one
ans3 = (cdf(z)) * 100

print(round(ans,2))
print(round(ans2,2))
print(round(ans3,2))