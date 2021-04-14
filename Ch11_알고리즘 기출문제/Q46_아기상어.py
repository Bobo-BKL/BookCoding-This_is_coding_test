from collections import deque

little_shark = 2
little_shark_eats = 0

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    global data, n
    visited = [[False] * n for _ in range(n)]
    results = []

    q = deque()
    q.append((0, x, y))

    while q:
        cost, x, y= q.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                if data[next_x][next_y] <= little_shark:
                    q.append((cost + 1, next_x, next_y))
                    visited[next_x][next_y] = True

                    if 0 < data[next_x][next_y] < little_shark:
                        results.append((cost + 1, next_x, next_y))

    if not results: return None
    else:
        results.sort()
        return results[0]

def eating_process(fish):
    global data, little_shark, little_shark_eats

    if not fish: return None

    cost, x, y = fish
    data[x][y] = 0
    little_shark_eats += 1
    if little_shark_eats == little_shark: 
        little_shark += 1
        little_shark_eats = 0
    return (cost, x, y)


##
fish_now_x = fish_now_y = 0
total_time_waste = 0

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            fish_now_x, fish_now_y = i, j
            data[i][j] = 0

while True:
    result = eating_process(bfs(fish_now_x, fish_now_y))

    if not result: break
    dist, fish_now_x, fish_now_y = result
    total_time_waste += dist

print(total_time_waste)