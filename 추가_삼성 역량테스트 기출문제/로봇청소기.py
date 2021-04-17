n, m = map(int, input().split())
x, y, dir = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    data[x][y] = 2

    is_succeed = False
    ndir = dir
    for _ in range(4):
        ndir = ndir - 1 if ndir > 0 else 3

        nx = x + dx[ndir]
        ny = y + dy[ndir]

        if data[nx][ny] == 0:
            x, y, dir = nx, ny, ndir
            is_succeed = True
            break

    if not is_succeed:
        x -= dx[dir]
        y -= dy[dir]

        if data[x][y] == 1: break

result = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 2: result += 1

print(result)