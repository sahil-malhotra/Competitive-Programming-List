#INOI1301

import sys

def f(i, forward):
    if i < 0:
        return -sys.maxsize
    elif i == 0 and forward == False:
        return 0
    elif mt[i][forward] != 'x':
        return mt[i][forward]
    elif forward:
        if i + 1 == n:
            mt[i][forward] = max(a[i-1] + f(i-1, False), a[i-2] + f(i-2, False))
        elif i + 2 == n:
            mt[i][forward] = max(a[i+1] + f(i+1, False), a[i-1] + f(i-1, False), a[i-2] + f(i-2, False))
        elif i + 2 < n:
            mt[i][forward] = max(a[i+2] + f(i+2, True), a[i+1] + f(i+1, True), a[i-1] + f(i-1, False), a[i-2] + f(i-2, False))
        return mt[i][forward]
    else:
        mt[i][forward] = max(a[i - 1] + f(i - 1, False), a[i - 2] + f(i - 2, False))
        return mt[i][forward]

n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

sys.setrecursionlimit(2*n)

mt = [['x' for i in range(2)] for j in range(n)]

if k-1 == 0:
    print(max(0, f(k-1, True)))
elif n == 1:
    print(0)
else:
    print(f(k-1, True))
