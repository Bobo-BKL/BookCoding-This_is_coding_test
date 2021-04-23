from collections import deque
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def get_groups(data, n, l, r):
    groups = []
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue

            temp = [(i, j)]
            cnt_city = 1
            sum_people = data[i][j]

            # bfs
            q = deque([(i, j)])
            visited[i][j] = True

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(data[x][y] - data[nx][ny]) <= r:
                        visited[nx][ny] = True
                        temp.append((nx, ny))
                        q.append((nx, ny))
                        cnt_city += 1
                        sum_people += data[nx][ny]

            # save
            if len(temp) <= 1: continue
            groups.append((sum_people // cnt_city, temp))

    return groups


def renew_people(data, groups):
    for people, group in groups:
        for x, y in group:
            data[x][y] = people


def solutions():
    result = 0

    n, l, r = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    while True:
        # 연합군 구하기
        groups = get_groups(data, n, l, r)
        if len(groups) < 1: break

        # 연합군 별로 인구수 재계산
        renew_people(data, groups)

        result += 1

    return result


print(solutions())
