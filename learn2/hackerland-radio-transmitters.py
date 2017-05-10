
def find_mid(s):
    # first house in the range
    sd = a[s]
    for i in range(s+1, n):
        if a[i] - sd > k2:
            return i-1
    return -1


# find next house w/o coverage
def find_next(m):
    # house with transmitter
    md = a[m]
    for i in range(m+1, n):
        if a[i] - md > k2:
            return i
    return -1


def find():
    s = 0
    while True:
        x = find_mid(s)
        if x < 0:
            #print(f'last place at house {s}, dist {a[s]}')
            yield s
            break
        #print(f'place at house {x}, dist {a[x]}')
        yield x
        s = find_next(x)
        if s < 0:
            break
        #print(f'next house {s}, dist {a[s]}')

n = 5 # num houses
k = 1 # range
a = [1, 2, 3, 4, 5]

#n = 8
#k = 2
#a = [7, 2, 4, 6, 5, 9, 12, 11]

k2 = 1 + k//2
print('half dist', k2)
a = sorted(a)
print(a)

f = [x for x in find()]
print(f)
print(len(f))

