INF = int(1e9)

graph = [
                [],
                [0, 0, 4, INF, 6],
                [0, 3, 0, 7, INF],
                [0, 5, INF, 0, 4],
                [0, INF, INF, 2, 0]
]

for k in range(1, len(graph)):
    for i in range(1, len(graph)):
        for j in range(1, len(graph)):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
           
for g in graph[1:]:
    print(g[1:])