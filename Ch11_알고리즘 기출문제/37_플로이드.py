n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(graph[a][b], cost)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j: continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        value = graph[i][j] if graph[i][j] != INF else 0
        if j == n: print(value)
        else: print(value, end = ' ')