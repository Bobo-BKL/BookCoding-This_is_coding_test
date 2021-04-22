from collections import deque
import copy

ps, q = map(int, input().split())
n = pow(2, ps)
ices = [list(map(int, input().split())) for _ in range(n)]
L = list(map(int, input().split()))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def turn_sector(size, cube):
    temp = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp[j][size - i - 1] = cube[i][j]
    return temp


def recurr_devider(row_start, row_end, col_start, col_end, cnt, p):
    global ices
    
    # 원하는 길이가 나올 경우
    if p == cnt:
        # copy
        temp = [ices[i][col_start:col_end] for i in range(row_start, row_end)]
        # turn
        temp = turn_sector(pow(2, cnt), temp)
        # paste
        tmp_cnt = 0
        for i in range(row_start, row_end):
            ices[i][col_start:col_end] = temp[tmp_cnt]
            tmp_cnt += 1

    # 원하는 길이가 아직 안나왔을 경우
    else:
        row_middle = (row_start + row_end) // 2
        col_middle = (col_start + col_end) // 2
        # 왼쪽 위
        recurr_devider(row_start, row_middle, col_start, col_middle, cnt - 1, p)
        # 오른쪽 위
        recurr_devider(row_start, row_middle, col_middle, col_end, cnt - 1, p)
        # 왼쪽 아래
        recurr_devider(row_middle, row_end, col_start, col_middle, cnt - 1, p)
        # 오른쪽 아래
        recurr_devider(row_middle, row_end, col_middle, col_end, cnt - 1, p)


def ice_get_small():
    global ices
    result = copy.deepcopy(ices)

    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n and ices[nx][ny] != 0:
                    cnt += 1
            if ices[i][j] != 0 and cnt < 3:
                result[i][j] -= 1
    ices = result


def make_ice_melt():
    for l in L:
        # sector clockwise turn
        if l != 0: recurr_devider(0, n, 0, n, ps, l)

        # ice shrinks
        ice_get_small()


def count_ice():
    result = 0
    for ice in ices:
        result += sum(ice)
    return result


def bfs_icecube(graph, x, y):
    count = 1
    q = deque([(x, y)])
    graph[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (not graph[nx][ny]) and (ices[nx][ny] != 0):
                count += 1
                q.append((nx, ny))
                graph[nx][ny] = True

    return graph, count


def get_huge_ice():
    result = 0
    graph = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (not graph[i][j]) and (ices[i][j] != 0):
                graph, count = bfs_icecube(graph, i, j)
                result = max(result, count)

    return result


make_ice_melt()
print(count_ice())
print(get_huge_ice())
