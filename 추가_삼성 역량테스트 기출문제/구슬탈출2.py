from collections import deque
import copy

n, m = map(int, input().split())
blue_x = blue_y = red_x = red_y = 0
board = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            blue_x, blue_y = i, j
            board[i][j] = '.'
        elif board[i][j] == 'R':
            red_x, red_y = i, j
            board[i][j] = 0

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def get_min_chance():
    result = int(1e9)

    q = deque([(copy.deepcopy(board), red_x, red_y, blue_x, blue_y, 0)])
    while q:
        original, orx, ory, obx, oby, count = q.popleft()

        if count > 10: continue

        # 네 방향으로 돌리기
        for dir in range(4):
            # copy originals
            rx, ry, bx, by = orx, ory, obx, oby
            copied = copy.deepcopy(original)

            is_failed = False
            is_goaled = False
            # 구슬아 끝까지 가렴
            while True:
                temp = (rx, ry, bx, by)

                # red moves
                nrx, nry = rx + dx[dir], ry + dy[dir]
                # goal!
                if copied[nrx][nry] == 'O':
                    is_goaled = True
                # red can go forward!
                elif copied[nrx][nry] != '#' and (nrx, nry) != (bx, by):
                    rx, ry = nrx, nry
                    copied[nrx][nry] = count + 1

                # blue moves
                nbx, nby = bx + dx[dir], by + dy[dir]
                # failed!
                if copied[nbx][nby] == 'O':
                    is_failed = True
                # blue can go forward!
                elif copied[nbx][nby] != '#':
                    if is_goaled:
                        # if red goaled, see if blue goals too
                        while copied[nbx][nby] != '#':
                            if copied[nbx][nby] == 'O':
                                is_failed = True
                                break
                            nbx, nby = nbx + dx[dir], nby + dy[dir]
                    else:
                        if (nbx, nby) != (rx, ry):
                            bx, by = nbx, nby

                # if goal and not blue get in to the hole
                if is_failed: break
                if is_goaled:
                    result = min(result, count + 1)
                    break

                # if not moved, end of while state
                if temp == (rx, ry, bx, by): break

            if not (is_failed or is_goaled) and (orx, ory, obx, oby) != (rx, ry, bx, by):
                q.append((copied, rx, ry, bx, by, count + 1))

    if result > 10: return -1
    else: return result


print(get_min_chance())
