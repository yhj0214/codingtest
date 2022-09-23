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