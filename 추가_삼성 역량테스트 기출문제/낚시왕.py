n, m, s = map(int, input().split())
sharks = []
for _ in range(s):
    shark = [True]
    shark.extend(list(map(int, input().split())))
    shark[1] -= 1
    shark[2] -= 1
    shark[4] -= 1
    sharks.append(shark)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def catch_shark(human):
    global sharks
    result = 0

    sharks.sort(key=lambda x: (x[2], x[1]))
    for s_num in range(s):
        if sharks[s_num][0] and sharks[s_num][2] == human:
            result = sharks[s_num][5]
            sharks[s_num][0] = False
            break

    return result


def move_sharks():
    global sharks
    temp = [[[] for _ in range(m)] for _ in range(n)]

    # 상어야, 움직여라!
    for s_num in range(s):
        if not sharks[s_num][0]: continue
        tf, r, c, sp, d, z = sharks[s_num]
        for _ in range(sp):
            r += dx[d]
            c += dy[d]
            if r >= n:
                r = n - 2
                d = 0
            elif 0 > r:
                r = 1
                d = 1
            elif c >= m:
                c = m - 2
                d = 3
            elif 0 > c:
                c = 1
                d = 2
        sharks[s_num] = [tf, r, c, sp, d, z]
        temp[r][c].append(s_num)

    # 상어 겹치면 먹어야징
    for i in range(n):
        for j in range(m):
            if len(temp[i][j]) > 1:
                big_num = temp[i][j][0]
                for s_num in temp[i][j]:
                    if sharks[big_num][5] < sharks[s_num][5]:
                        sharks[big_num][0] = False
                        big_num = s_num
                    elif sharks[big_num][5] > sharks[s_num][5]:
                        sharks[s_num][0] = False


def is_sharks():
    for shark in sharks:
        if shark[0]: return True
    return False


def get_result():
    result = 0

    for human in range(m):
        # 상어가 없으면 더이상 볼 필요 없음
        if not is_sharks(): break

        # 사람있는 열에서 가장 가까운 상어 잡기
        result += catch_shark(human)
        
        # 상어 이동하기
        move_sharks()

    return result


print(get_result())
