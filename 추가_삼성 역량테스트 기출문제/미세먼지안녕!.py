n, m, t = map(int, input().split())
A = []

for _ in range(n):
    A.append(list(map(int, input().split())))

for k in range(n):
    if A[k][0] == -1:
        aircon = [k, k + 1]
        break

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def spread_polutions():
    global A
    sums = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if A[i][j] >= 5:
                poluted = A[i][j] // 5
                p_cnt = 0
                for di in range(4):
                    nx, ny = i + dx[di], j + dy[di]
                    if 0 <= nx < n and 0 <= ny < m and A[nx][ny] != -1:
                        sums[nx][ny] += poluted
                        p_cnt += 1
                sums[i][j] += A[i][j] - poluted * p_cnt
            else:
                sums[i][j] += A[i][j]
    A = sums


def activate_upper_aircon(airnum):
    global A
    # 맨왼쪽, 아래 방향
    for i in range(airnum - 2, -1, -1):
        A[i + 1][0] = A[i][0]
    # 맨위쪽, 왼 방향
    for i in range(1, m):
        A[0][i - 1] = A[0][i]
    # 맨오른쪽, 위 방향
    for i in range(1, airnum + 1):
        A[i - 1][m - 1] = A[i][m - 1]
    # 맨아래쪽, 오른 방향
    for i in range(m - 2, 0, -1):
        A[airnum][i + 1] = A[airnum][i]
        
    A[airnum][1] = 0


def activate_lower_aircon(airnum):
    global A
    # 맨왼쪽, 위 방향
    for i in range(airnum + 2, n):
        A[i - 1][0] = A[i][0]
    # 맨아래쪽, 왼 방향
    for i in range(1, m):
        A[n - 1][i - 1] = A[n - 1][i]
    # 맨오른쪽, 아래 방향
    for i in range(n - 2, airnum - 1, -1):
        A[i + 1][m - 1] = A[i][m - 1]
    # 맨위쪽, 오른 방향
    for i in range(m - 2, 0, -1):
        A[airnum][i + 1] = A[airnum][i]

    A[airnum][1] = 0


def count_poluted():
    result = 0
    for i in range(n):
        for j in range(m):
            result += A[i][j]
    return result


for _ in range(t):
    spread_polutions()
    activate_upper_aircon(aircon[0])
    activate_lower_aircon(aircon[1])

print(count_poluted() + 2)