from collections import deque
b = int(input())
n, m = 6, 4
blocks = [list(map(int, input().split())) for _ in range(b)]

green_board = [[False] * m for _ in range(n)]
blue_board = [[False] * m for _ in range(n)]


def put_block(board, block):
    result = 0
    t, x, y = block
    is_put = False
    # 블록 놓기
    if t == 1:
        for i in range(1, n):
            if board[i][y]:
                board[i - 1][y] = is_put = True
                break
        if not is_put: board[n - 1][y] = True
    elif t == 2:
        for i in range(1, n):
            if board[i][y] or board[i][y + 1]:
                board[i - 1][y] = board[i - 1][y + 1] = is_put = True
                break
        if not is_put: board[n - 1][y] = board[n - 1][y + 1] = True
    elif t == 3:
        for i in range(2, n):
            if board[i][y]:
                board[i - 1][y] = board[i - 2][y] = is_put = True
                break
        if not is_put: board[n - 1][y] = board[n - 2][y] = True

    # 행 가득찼나 보기
    fulls = [False] * n
    spoiled = 0
    for i in range(n - 1, -1, -1):
        cnt = 0
        for j in range(m):
            if board[i][j]: cnt += 1
        if cnt == m: fulls[i] = True
        if i < 2 and cnt > 0: spoiled += 1

    # 행 가득차면 지우기
    temp = deque()
    for i in range(n - 1, -1, -1):
        if not fulls[i]:
            temp.append(board[i])
        else:
            result += 1
            spoiled -= 1

    # 남은 행이 4줄이 넘나 보기
    if len(temp) > 4 and spoiled > 0:
        [temp.popleft() for _ in range(spoiled)]
    # 남는 행 붙여넣기
    for i in range(n - 1, -1, -1):
        if temp: board[i] = temp.popleft()
        else:
            board[i] = [False] * m

    return result


def process():
    global green_board, blue_board
    result = 0

    for block in blocks:
        result += put_block(green_board, block)
        t, x, y = block
        if t == 1:
            result += put_block(blue_board, [1, y, 4 - x - 1])
        elif t == 2:
            result += put_block(blue_board, [3, y, 4 - x - 1])
        else:
            result += put_block(blue_board, [2, y, 4 - x - 2])

    return result


def get_blocks():
    result = 0
    for i in range(n):
        for j in range(m):
            if green_board[i][j]: result += 1
            if blue_board[i][j]: result += 1
    return result


print(process())
print(get_blocks())
