#RENT

import sys

t = int(input())

def p(mid, i):
    if orders[mid][0] > orders[i][0]+orders[i][1]:
        return True
    return False

def find_next(i):
    if orders[i][0]+orders[i][1] > orders[n-1][0]:
        return n
    
    lo = 0
    hi = n-1
    
    while lo < hi:
        mid = lo + (hi-lo)//2
        if p(mid, i):
            hi = mid
        else:
            lo = mid+1
    return lo


def f(i):
    if i == n:
        return 0
    elif mt[i] != -1:
        return mt[i]
    else:
        ind = find_next(i)
        mt[i] = max(orders[i][2] + f(ind), f(i+1))
        return mt[i]


while t > 0:
    n=int(input())
    orders = []
    
    for i in range(n):
        orders.append(list(map(int, input().split())))
    orders.sort(key=lambda x: x[0])

mt = [-1]*n
sys.setrecursionlimit(n+3)
print(f(0))
t-=1
