n = 6
k = 3
a = [1, 3, 2, 6, 1, 2]

c = 0
for j in range(n):
    for i in range(j):
        if (a[i] + a[j]) % k == 0:
            c += 1
print(c)

p = [(i, j) for j in range(n) for i in range(j) if (a[i] + a[j]) % k == 0]
print(p)
print(len(p))
