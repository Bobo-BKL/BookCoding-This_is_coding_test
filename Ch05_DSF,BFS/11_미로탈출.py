from collections import deque

n, m = map(int, input().split())
 
data = []
for _ in range(n):
    data.append(list(map(int, input())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
  
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
     
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                         
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            
            if data[nx][ny] == 1 and  not (nx == 0 and ny == 0):
                queue.append((nx, ny))
                data[nx][ny] = data[x][y] + 1
                
    return data[n - 1][m - 1]
    
print(bfs(0, 0))
