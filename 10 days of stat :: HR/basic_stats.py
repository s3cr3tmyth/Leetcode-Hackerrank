from collections import Counter

X = [64630,11735,14216,99233,14470,4978,73429,38120,51135,67060]


def basic_stats(X):
    N = len(X)
    mean = sum(X) / N
    index = N // 2
    if N % 2:
        median =  sorted(X)[index]
    median =  sum(sorted(X)[index - 1:index + 1]) / 2
    c = Counter(X)
    mode = [k for k, v in c.items() if v == c.most_common(1)[0][1]]

    return mean, median, min(mode)



x,y,z = basic_stats(X)

print(x,'\n',y,'\n',z)



