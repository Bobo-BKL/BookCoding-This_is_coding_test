n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    data[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        
        if data[nx][ny] == 0: dfs(nx, ny)
        
result = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 0: 
            dfs(i, j)
            result += 1
            
print(result)
