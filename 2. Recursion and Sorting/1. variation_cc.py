#ZCO15002

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
j = 0
i = 0

while(j < n):
    
    if a[j] >= a[i] + k:
        i += 1
        count += n - j
    else:
        j += 1

print(count)
