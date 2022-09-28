
n, m = map(int, input().split())
inarr = []
answer = 0

for i in range(n):
    inarr.append(list(map(int, input())))

def dfs(inarr, y, x):
    
    if x<0 or y<0 or y>=n or x>=m:
        return
    if inarr[y][x] == 1:
        return

    if inarr[y][x] == 0:
        inarr[y][x] = 1
        dfs(inarr, y,x-1)
        dfs(inarr, y-1,x)
        dfs(inarr, y,x+1)
        dfs(inarr, y+1,x)
        return False
    return False

for y in range(n):
    for x in range(m):
        if inarr[y][x] == 0:
            answer += 1
            dfs(inarr, y, x)
print(answer)