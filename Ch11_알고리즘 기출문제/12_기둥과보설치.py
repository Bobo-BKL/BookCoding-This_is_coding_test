class Structures:
    def __init__(self, g = False, b = False): 
        self.gidoong = g
        self.bo = b
        
dx = [-1, 0, 1, 0, -1, 1, 1, -1, 0]
dy = [0, 1, 0, -1, -1, 1, -1, 1, 0]

def is_available(board, x, y, a):
    if a == 0:
        if y == 0 or (x > 0 and board[x - 1][y].bo) or (x < len(board) - 1 and board[x][y].bo) or (y > 0 and board[x][y - 1].gidoong): return True
    else:
        if (y > 0 and board[x][y - 1].gidoong) or ((x < len(board) - 1) and (y > 0) and board[x + 1][y - 1].gidoong) or ((0 < x < len(board) - 1) and board[x - 1][y].bo and board[x + 1][y].bo):  return True
        
    return False
        
def delete_frame(board, x, y, a):
    if a == 0: board[x][y].gidoong = False
    else: board[x][y].bo = False
    
    for i in range(9):
        if 0 <= (x + dx[i]) < len(board) and 0 <= (y + dy[i]) < len(board):
            nx = x + dx[i]
            ny = y + dy[i]
        else: continue

        if not board[nx][ny].gidoong and not board[nx][ny].bo: continue
        
        if (board[nx][ny].gidoong and not is_available(board, nx, ny, 0)) or (board[nx][ny].bo and not is_available(board, nx, ny, 1)): 
            if a == 0: board[x][y].gidoong = True
            else: board[x][y].bo = True
            break
            
def add_frame(board, x, y, a):
    if is_available(board, x, y, a): 
        if a == 0: board[x][y].gidoong = True
        else: board[x][y].bo = True

def solution(n, build_frame):
    answer = []
    board = [[Structures() for _ in range(n + 1)] for _ in range(n + 1)]
    
    for frame in build_frame:
        x, y, a, b = frame
        
        if b == 0:
            delete_frame(board, x, y, a)
        else:
            add_frame(board, x, y, a)
        
    for i in range(n + 1):
        for j in range(n + 1):
            if board[i][j].gidoong: answer.append([i, j, 0])
            if board[i][j].bo: answer.append([i, j, 1])
    
    return answer
    
build_frame = [
[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
[5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]
]
build_frame2 = [
[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
[1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
[1, 1, 1, 0], [2, 2, 0, 1]
]
n = 5
print(solution(n, build_frame2))

test_frame = [
[0, 0, 0, 1], [0, 1, 1, 1], [2, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1],
[2, 2, 0, 1], [2, 3, 1, 1], [3, 3, 1, 1], [4, 3, 1, 1], 
[5, 0, 0, 1], [5, 1, 0, 1], [5, 2, 0, 1], [4, 3, 1, 1],
[3, 3, 1, 1], [5, 2, 0, 0]
]

print(solution(5, test_frame))