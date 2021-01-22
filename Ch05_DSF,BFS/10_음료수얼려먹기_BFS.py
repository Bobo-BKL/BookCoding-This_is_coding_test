from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 1: return False
    
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
                    
    return True
    
result = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j): result += 1
        
print(result)
