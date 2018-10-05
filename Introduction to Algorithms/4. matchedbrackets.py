#ZCO12001

n = int(input())
nums = list(map(int, input().split()))
open = 0
count = 0
first_pos = 0
this_pos = 0
max_count = 0
max_depth = 0

for i in range(n):
    count += 1
    
    if nums[i] == 1:
        open += 1
        
        if open > max_depth:
            max_depth = open
            first_pos = i+1

else:
    open -= 1
    
    if open == 0:
        if count > max_count:
            max_count = count
            this_pos = i-count+2
        
        count = 0

print(" ".join(map(str, [max_depth, first_pos, max_count, this_pos])))
