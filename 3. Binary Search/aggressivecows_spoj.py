#AGGRCOW

t = int(input())

def num_cows(diff, a, c):
    count = 1
    curr = 0
    for i in range(1,n):
        if a[i] - a[curr] >= diff:
            count += 1
            curr = i
            if count >= c:
                return True
    return False


while t:
    n, c = map(int, input().split())
    x = []
    for i in range(n):
        x.append(int(input()))
    x.sort()


lo = 0
    hi = x[n-1]
    while lo < hi:
        mid = lo + (hi-lo+1)//2
        #print(mid)
        num = num_cows(mid, x, c)
        
        if num:
            lo = mid
        else:
            hi = mid - 1

print(lo)

    t-=1
