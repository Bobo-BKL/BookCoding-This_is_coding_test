from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def solution(board):
    answer = int(1e9)
    n = len(board)

    q = deque([(0, 0, -1, 0)])

    while q:
        x, y, before_dir, val = q.popleft()

        if (x, y) == (n - 1, n - 1):
            answer = min(answer, val)
            continue

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                temp_val = val + 100
                if before_dir != -1 and before_dir != dir:
                    temp_val += 500

                if temp_val < answer:
                    if board[nx][ny] == 0 or board[nx][ny] >= temp_val:
                        board[nx][ny] = temp_val
                        q.append((nx, ny, dir, temp_val))

    return answer


print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
