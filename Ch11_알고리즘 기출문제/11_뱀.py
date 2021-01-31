from collections import deque

# n: 보드 크기
n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

# k: 사과 개수
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = -1
    
# l: 뱀의 방향 정보 개수    
l = int(input())
directions = deque()
for _ in range(l):
    x, c = input().split()
    directions.append((int(x), 1 if c == 'D' else -1))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def gogo_snake():
    snake_dir = 0
    snake_x = 1
    snake_y = 1
    board[snake_x][snake_y] = 1
    seconds = 0
    
    q = deque()
    q.append((snake_x, snake_y))

    end_time = -1
    change_dir = -1
    if directions: end_time, change_dir = directions.popleft()
        
    while True:
        seconds += 1
        snake_x += dx[snake_dir]
        snake_y += dy[snake_dir]
        if snake_x < 1 or snake_x > n or snake_y < 1 or snake_y > n or board[snake_x][snake_y] > 0: return seconds
        q.append((snake_x, snake_y))
        
        if board[snake_x][snake_y] == 0:
            x, y = q.popleft()
            board[x][y] = 0
        board[snake_x][snake_y] = 1
        
        if seconds == end_time:    
            snake_dir = (snake_dir + change_dir) % 4
            if directions: end_time, change_dir = directions.popleft()
            else: end_time = -1
    
print(gogo_snake())