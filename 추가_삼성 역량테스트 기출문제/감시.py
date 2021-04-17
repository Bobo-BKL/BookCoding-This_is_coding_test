import copy
n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
directions = [
    [],
    [[0], [1], [2], [3]],
    [(0, 2), (1, 3)],
    [(0, 1), (1, 2), (2, 3), (3, 0)],
    [(3, 0, 1), (0, 1, 2), (1, 2, 3), (2, 3, 0)],
    [(0, 1, 2, 3)]
]


def get_colored(array, curr_x, curr_y, direction):
    for dirs in direction:
        x, y = curr_x, curr_y
        while True:
            nx = x + dx[dirs]
            ny = y + dy[dirs]

            if not (0 <= nx < n and 0 <= ny < m): break
            if array[nx][ny] == 6: break
            if array[nx][ny] == 0: array[nx][ny] = 7
            x, y = nx, ny

    return array


def cnt_not_colored(array):
    res = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0: res += 1
    return res


result = int(1e9)
def recurr(array, index):
    global result
    while index < n * m:
        curr_x, curr_y = index // m, index % m
        if not(1 <= array[curr_x][curr_y] <= 5):
            index += 1
            continue

        cctv_num = array[curr_x][curr_y]
        for direction in directions[cctv_num]:
            arr_copy = get_colored(copy.deepcopy(array), curr_x, curr_y, direction)
            recurr(arr_copy, index + 1)
        index += 1

    result = min(result, cnt_not_colored(array))


recurr(data, 0)
print(result)
