
#INOI1401

import sys

def paths(i, j, limit, di):
    
    if grid[i][j] == 0:
        return 0
    
    elif i == r-1 and j == c-1:
        return 1
    
    elif dp[i][j][limit][di] != -1:
        return dp[i][j][limit][di]
    
    elif i == r-1:
        if limit == d and di == False:
            return 0
        else:
            if di:
                dp[i][j][limit][di] = paths(i, j + 1, 1, False)%20011
            else:
                dp[i][j][limit][di] = paths(i, j + 1, limit+1, False)%20011
            return dp[i][j][limit][di]

elif j == c-1:
    if limit == d and di == True:
        return 0
        else:
            if not di:
                dp[i][j][limit][di] = paths(i+1, j, 1, True)%20011
            else:
                dp[i][j][limit][di] = paths(i+1, j, limit+1, True)%20011
            return dp[i][j][limit][di]


else:
    if limit == d and di == True:
        dp[i][j][limit][di] = paths(i, j+1, 1, False)%20011
        
        elif limit == d and di == False:
            dp[i][j][limit][di] = paths(i+1, j, 1, True)%20011

    else:
        if di:
            dp[i][j][limit][di] = (paths(i, j+1, 1, False)%20011 + paths(i+1, j, limit+1, True)%20011)%20011
            else:
                dp[i][j][limit][di] = (paths(i, j+1, limit+1, False)%20011 + paths(i+1, j, 1, True)%20011)%20011
return dp[i][j][limit][di]

def easy_paths(i, j):
    if grid[i][j] == 0:
        return 0
    elif i == r-1 and j == c-1:
        return 1
    elif i == r-1:
        dp2[i][j] = easy_paths(i, j + 1) % 20011
    elif j == c-1:
        dp2[i][j] = easy_paths(i + 1, j) % 20011
    elif dp2[i][j] != -1:
        return dp2[i][j]
    else:
        dp2[i][j] = (easy_paths(i+1,j)%20011 + easy_paths(i, j+1)%20011)%20011
    return dp2[i][j]

r, c, d = map(int, input().split())
grid = []

for i in range(r):
    grid.append(list(map(int, input().split())))

dp = []
dp2 = []

sys.setrecursionlimit(300*300*300*2)

if d == max(r, c) - 1:
    for i in range(r):
        dp2.append([])
        for j in range(c):
            dp2[i].append(-1)
    print(easy_paths(0,0))

else:
    for i in range(r):
        dp.append([])
        for j in range(c):
            dp[i].append([])
            for limit in range(d + 1):
                dp[i][j].append([])
                for di in range(2):
                    dp[i][j][limit].append(-1)
    print(paths(0,0,0,0))
