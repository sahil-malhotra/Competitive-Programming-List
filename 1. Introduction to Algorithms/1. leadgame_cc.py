#LEADGAME

n = int(input())
total_s = 0
total_t = 0
max_diff = 0
player = 0

for i in range(n):
    p1, p2 = input().split()
    p1, p2 = int(p1), int(p2)
    total_s += p1
    total_t += p2
    curr_diff = total_s-total_t
    
    if abs(curr_diff) > max_diff:
        if curr_diff > 0:
            player = 1
        else:
            player = 2
        max_diff = abs(curr_diff)

print(player, max_diff)
