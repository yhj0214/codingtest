from array import array
from glob import glob


n, m = map(int, input().split())
x, y, direction = map(int, input().split())
answerarr = [[0]*m for _ in range(n)]

answerarr[x][y] = 1

mapinfo = []
for i in range(n):
    mapinfo.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction = direction - 1
    if direction == -1:
        direction =3 

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if answerarr[nx][ny] == 0 and mapinfo[nx][ny] == 0:
        answerarr[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x-dx[direction]
        ny = y-dy[direction]

        if mapinfo[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_time = 0

        
print(count)
