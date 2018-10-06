#ZCO12002

import sys

n, x, y = map(int, input().split())
contests = []

for i in range(n):
    start, end = map(int, input().split())
    contests.append([start, end])

v = sorted(list(map(int, input().split())))
w = sorted(list(map(int, input().split())))

ans = sys.maxsize
a=0

def binary_search_v(ele):
    l = 0
    u = x - 1
    
    if ele < v[0]:
        return -1

    while l <= u:
        m = (u + l) // 2
        
        if ele == v[m]:
            return m
        
        elif ele < v[m]:
            u = m - 1
        
        else:
            l = m + 1

return l-1

def binary_search_w(ele):
    l = 0
    u = y - 1
    
    if ele > w[u]:
        return -1

    while l <= u:
        m = (u + l) // 2
        
        if ele == w[m]:
            return m
        
        elif ele < w[m]:
            u = m - 1
        
        else:
            l = m + 1

return l

for contest in contests:
    
    matched_v = binary_search_v(contest[0])
    matched_w = binary_search_w(contest[1])
    
    if matched_w != -1 and matched_v != -1:
        ans = min(ans, w[matched_w]-v[matched_v]+1)

print(ans)
