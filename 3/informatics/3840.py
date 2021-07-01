a = [int(i) for i in input().split()]
d = list(reversed(a))
for i in range(len(d)):
    print(d[i], end=' ')