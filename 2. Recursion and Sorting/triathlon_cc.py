n = int(input())
people = []
ans = 0

for i in range(n):
    a, b, c = map(int, input().split())
    people.append([a, b+c])

people.sort(key=lambda x:x[1], reverse=True)
first_task=0

for i in range(n):
    first_task += people[i][0]
    ans = max(ans,first_task + people[i][1])

print(ans)
