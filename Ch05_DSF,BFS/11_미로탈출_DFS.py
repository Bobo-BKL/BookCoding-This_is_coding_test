n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            dfs(nx, ny)
            
dfs(0, 0)

print(graph[n - 1][m - 1])
