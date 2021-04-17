from collections import deque
import copy

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def bfs(graph):
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2: q.append((i, j))

    while q:
        x, y = q.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))

    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: result += 1

    return result

answer = 0
# wall 1
for wall1 in range(n * m):
    if data[wall1 // m][wall1 % m] != 0: continue
    # wall 2
    for wall2 in range(wall1 + 1, n * m):
        if data[wall2 // m][wall2 % m] != 0: continue
        # wall 3
        for wall3 in range(wall2 + 1, n * m):
            if data[wall3 // m][wall3 % m] != 0: continue
            copied = copy.deepcopy(data)
            copied[wall1 // m][wall1 % m] = copied[wall2 // m][wall2 % m] = copied[wall3 // m][wall3 % m] = 1

            cnt = bfs(copied)
            answer = max(answer, cnt)

print(answer)