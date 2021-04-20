from collections import deque

n, m, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
turns = [list(map(int, input().split())) for _ in range(t)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(x, y, num):
    global data
    q = deque([(x, y)])
    is_to_0 = False

    while q:
        x, y = q.popleft()

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if ny >= m: ny = 0
            elif ny < 0: ny = m - 1

            if 0 <= nx < n and data[nx][ny] == num:  # 인접하고 서로 같음
                is_to_0 = True
                q.append((nx, ny))
                data[nx][ny] = 0

    if is_to_0:
        data[x][y] = 0

    return data[x][y]


def cal_board():
    global data
    for x, d, k in turns:
        # 원판 돌리기
        for i in range(n):
            if (i + 1) % x != 0: continue
            temp = [0] * m
            if d == 0:  # 시계 방향
                for j in range(m):
                    temp[(j + k) % m] = data[i][j]
            else:  # 반시계 방향
                for j in range(m):
                    temp[j - k] = data[i][j]
            data[i] = temp

        # 각 원판 돌며 인접수 찾기
        is_no_num = True
        is_same_and_deleted = False
        left_sum = lefts = 0
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0: continue  # 해당칸에 수 없음
                is_no_num = False

                # 인접 찾기
                res = bfs(i, j, data[i][j])
                if res != 0:
                    left_sum += res
                    lefts += 1
                else: is_same_and_deleted = True

        if is_no_num: return True

        # 수는 있지만, 인접 & 같은 수가 없는 경우
        if not is_same_and_deleted:
            average = left_sum / lefts
            for i in range(n):
                for j in range(m):
                    if data[i][j] != 0:
                        if data[i][j] > average: data[i][j] -= 1
                        elif data[i][j] < average: data[i][j] += 1

    return False


if cal_board(): print(0)
else:
    sums = 0
    for i in range(n):
        sums += sum(data[i])
    print(sums)
