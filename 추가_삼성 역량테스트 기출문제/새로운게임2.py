from collections import deque
n, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
board_horses = [[deque() for _ in range(n)] for _ in range(n)]
horse_infos = []
for i in range(k):
    x, y, dir = map(lambda x: int(x) - 1, input().split())
    board_horses[x][y].append(i)
    horse_infos.append([x, y, dir])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def white_or_red(h_num, nx, ny):
    global board_horses, horse_infos
    x, y, _ = horse_infos[h_num]

    leave = deque()
    move = deque()
    found = False

    # 원래 있던 자리에서 움직일 말 분류
    while board_horses[x][y]:
        element = board_horses[x][y].popleft()
        if element == h_num: found = True
        if found:
            move.append(element)
            horse_infos[element][0], horse_infos[element][1] = nx, ny
        else:
            leave.append(element)
    board_horses[x][y] = leave

    if board[nx][ny] != 0: move.reverse()  # red
    board_horses[nx][ny].extend(move)  # 움직일 말 새 자리에 병합

    # 움직인 자리에 4개 이상인가?
    if len(board_horses[nx][ny]) >= 4: return True
    return False


def move_horse(h_num):
    global board_horses, horse_infos

    x, y, dir = horse_infos[h_num]
    nx, ny = x + dx[dir], y + dy[dir]

    # white or red
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
        if white_or_red(h_num, nx, ny): return True

    else:  # out or blue
        if dir == 0: ndir = 1
        elif dir == 1: ndir = 0
        elif dir == 2: ndir = 3
        else: ndir = 2

        horse_infos[h_num] = [x, y, ndir]

        # 앞칸 이동 가능하면 이동
        nx, ny = x + dx[ndir], y + dy[ndir]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
            if white_or_red(h_num, nx, ny): return True

    return False


def get_result():
    result = 0

    while result <= 1000:
        result += 1
        is_horse_4 = False
        for h_num in range(k):
            if move_horse(h_num):
                is_horse_4 = True
                break
        if is_horse_4: break

    return result


r = get_result()
if r > 1000: print(-1)
else: print(r)