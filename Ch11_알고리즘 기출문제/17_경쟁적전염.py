from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, k = map(int, input().split())

board = []
q = deque()
for i in range(n):
    board.append(list(map(int, input().split())))
    
    for j in range(n):
        if board[i][j] != 0: q.append((board[i][j], i, j, 0))
        
s, x, y = map(int, input().split())

while q:
    virus, vx, vy, sec = q.popleft()
    
    if sec + 1 > s: break
    
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        
        if board[nx][ny] == 0:
            board[nx][ny] = virus
            q.append((virus, nx, ny, sec + 1))
    
print(board[x - 1][y - 1])