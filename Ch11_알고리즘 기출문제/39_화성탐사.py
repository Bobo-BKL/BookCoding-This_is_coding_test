import heapq

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

INF = int(1e9)
result = [[INF] * n for _ in range(n)]

q = []
heapq.heappush(q, (graph[0][0], 0, 0))
result[0][0] = graph[0][0]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
while q:
    now_cost, x, y = heapq.heappop(q)
    if now_cost > result[x][y]: continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            next_cost = now_cost + graph[nx][ny]
            if next_cost < result[nx][ny]:
                result[nx][ny] = next_cost
                heapq.heappush(q, (next_cost, nx, ny))

print(result[n - 1][n - 1])