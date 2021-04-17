tetrominoes = [
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, -2], [1, -1], [1, 0]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [1, 0]],
    [[0, 0], [1, 0], [2, 0], [2, -1]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [1, -1], [1, 0]],
    [[0, 0], [1, -1], [1, 0], [2, -1]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 0]],
    [[0, 0], [1, -1], [1, 0], [1, 1]],
    [[0, 0], [1, -1], [1, 0], [2, 0]]
]

n, m = map(int, input().split())
data = []
result = 0
for _ in range(n):
    data.append(list(map(int, input().split())))

for x in range(n):
    for y in range(m):
        # start_point = [y, x]
        for tetromino in tetrominoes:
            is_possible = True
            # 블록이 종이 안에 들어오는 지 확인하기
            for i in range(4):
                nx = x + tetromino[i][0]
                ny = y + tetromino[i][1]
                if not (0 <= nx < n and 0 <= ny < m):
                    is_possible = False
                    break
            # 블록이 종이 안에 들어오면 값 계산하기
            if is_possible:
                temp = 0
                for i in range(4):
                    temp += data[x + tetromino[i][0]][y + tetromino[i][1]]
                result = max(temp, result)

print(result)