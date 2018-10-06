#VOTERS

from collections import defaultdict # 0.23 sec

n1, n2, n3 = map(int, input().split())

num_freq = defaultdict(int)
ans = []

for i in range(n1+n2+n3):
    num = int(input())
    num_freq[num] += 1

for key in sorted(num_freq.keys()):
    if num_freq[key] > 1:
        ans.append(key)

print(len(ans))

for num in ans:
    print(num)
