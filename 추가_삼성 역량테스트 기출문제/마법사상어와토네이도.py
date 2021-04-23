sand_spread = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, -1, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def sand_redistributions(data, n, x, y):
    get_out = 0
    total_sand = left = data[x][y]

    if total_sand == 0: return 0

    ox, oy = x - 2, y - 2
    for i in range(5):
        for j in range(5):
            nx, ny = ox + i, oy + j
            if sand_spread[i][j] == 0:  # 비율조정 값이 없음
                continue
            elif sand_spread[i][j] == -1:  # a점임
                ax, ay = nx, ny
                continue
            used = int(total_sand * sand_spread[i][j])
            if 0 <= nx < n and 0 <= ny < n:
                data[nx][ny] += used
            else:
                get_out += used
            left -= used

    # a
    if 0 <= ax < n and 0 <= ay < n:
        data[ax][ay] += left
    else: get_out += left

    data[x][y] = 0

    return get_out


def get_out_sand():
    global sand_spread
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    current_x = current_y = n // 2
    p_cnt = 0

    while True:
        for dir in range(4):
            if dir % 2 == 0: p_cnt += 1
            for _ in range(p_cnt):
                current_x, current_y = current_x + dx[dir], current_y + dy[dir]
                result += sand_redistributions(data, n, current_x, current_y)
                if current_x == 0 and current_y == 0: return result
            sand_spread = list(zip(*sand_spread))[::-1]


print(get_out_sand())
