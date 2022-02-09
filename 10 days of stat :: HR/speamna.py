def get_rank(X, n):
    x_rank = dict((x, i + 1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]


X = [10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2]

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rx = get_rank(X, n)
ry = get_rank(Y, n)

d = [(rx[i] - ry[i]) ** 2 for i in range(n)]
rxy = 1 - (6 * sum(d)) / (n * (n * n - 1))

print('%.3f' % rxy)