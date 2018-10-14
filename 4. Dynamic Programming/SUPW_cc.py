#ZCO14002

import sys

def time(i, free):
    if free == 3:
        return sys.maxsize
    elif i == n:
        return 0
    elif mt[i][free] != -1:
        return mt[i][free]
    else:
        mt[i][free] =  min(minutes[i] + time(i+1, 0), time(i+1, free+1))
        return mt[i][free]

n = int(input().strip())
minutes = list(map(int, input().strip().split()))

sys.setrecursionlimit(3*n)

mt = [[-1 for i in range(3)] for j in range(n)]

print(time(0, 0))
