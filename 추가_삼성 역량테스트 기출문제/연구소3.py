from itertools import combinations
import copy
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(array, vrs):
    global result
    seconds = 0
    q = deque(vrs)
    vrs_count = 0

    while q:
        if virus_total == vrs_count: break
        x, y = q.popleft()
        time = array[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if array[nx][ny] == -2:
                    array[nx][ny] = time + 1
                    q.append((nx, ny))
                    seconds = time + 1

                elif array[nx][ny] == INF:
                    array[nx][ny] = time + 1
                    q.append((nx, ny))
                    seconds = time + 1
                    vrs_count += 1

        if seconds >= result: return

    for i in range(n):
        for j in range(n):
            if array[i][j] == INF: return

    result = seconds


viruses = []
virus_total = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            viruses.append((i, j))
            data[i][j] = -2
        elif data[i][j] == 1:
            data[i][j] = -1
        else:
            data[i][j] = INF
            virus_total += 1

result = INF
for virus in list(combinations(viruses, m)):
    copied = copy.deepcopy(data)
    for x, y in virus:
        copied[x][y] = 0

    bfs(copied, virus)
    if result == 0: break

if result >= INF: print(-1)
else: print(result)