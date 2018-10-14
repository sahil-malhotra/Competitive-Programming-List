#ZCO12004

import sys

def fun(index, chosen):
    
    global take_last
    
    if index == n:
        return 0
    
    elif mt[index][chosen] != -1:
        return mt[index][chosen]
    
    elif index == n-1 and take_last:
        return cost[index]
    
    elif chosen:
        mt[index][chosen] = min(cost[index] + fun(index+1, True), fun(index+1, False))
        return mt[index][chosen]
    
    else:
        mt[index][chosen] = cost[index] + fun(index+1, True)
        return mt[index][chosen]


n = int(input().strip())
cost = list(map(int, input().strip().split()))

sys.setrecursionlimit(2*n)

# Case 1 where we DO NOT take cost for zeroth index
take_last = True      # Strictly include the last cost
mt = [[-1 for i in range(2)] for j in range(n)]
val1 = fun(1, False)

# Case 2 where we DO take cost for zeroth index
take_last = False    # The last cost can be included or excluded
mt = [[-1 for l in range(2)] for m in range(n)]
val2 = fun(0, False)

print(min(val1, val2))
