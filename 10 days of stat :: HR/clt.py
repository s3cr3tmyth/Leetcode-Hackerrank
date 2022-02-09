import math

### 1 problem
# mu, sd = 205, 15
# n = 49
# mu_ = n * mu
# sd_ =  math.sqrt(n) * sd
# x = 9800

# cdf = lambda x: 0.5 * (1 + math.erf((x - mu_) / (sd_ * (2 ** 0.5))))

# print(round(cdf(x),4))

### prob2

# mu, sd = 2.4, 2.0
# n = 100
# mu_ = n * mu
# sd_ =  math.sqrt(n) * sd
# x = 250

# cdf = lambda x: 0.5 * (1 + math.erf((x - mu_) / (sd_ * (2 ** 0.5))))

# print(round(cdf(x),4))

### problem 3
# Here population mean is given so converting to sample mean and same for variance

# true population distribution
mu, sd = 500, 80
n = 100

# sample mean distribution
muS, sds = mu, sd/(n**0.5)

### The z-score is a factor telling you with what probability you land in an interval of z standard deviations away from the mean 
# (in both directions) 
z = 1.96
# interval = .95


# confidence intervals of sample mean dist
A = mu - (z*sds)
B = mu + (z*sds)

print(round(A,2))
print(round(B,2))
