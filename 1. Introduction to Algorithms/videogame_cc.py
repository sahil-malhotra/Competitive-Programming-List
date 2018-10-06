#ZCO14001

n, h = map(int, input().split())
stack = list(map(int, input().split()))
cmds = list(map(int, input().split()))
stack_pos = 0
picked = False

for i in range(len(cmds)):
    if cmds[i] == 1:
        if stack_pos > 0:
            stack_pos -= 1

elif cmds[i] == 2:
    if stack_pos < n-1:
        stack_pos += 1
    
    elif cmds[i] == 3:
        if not picked and stack[stack_pos] != 0:
            picked = True
            stack[stack_pos] -= 1

elif cmds[i] == 4:
    if picked and stack[stack_pos] < h:
        picked = False
            stack[stack_pos] += 1

print(" ".join(map(str, stack)))
