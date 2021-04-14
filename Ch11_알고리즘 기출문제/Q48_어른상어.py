import copy

n, m, cnt = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dir = list(map(lambda x : int(x) - 1, input().split()))
dir.insert(0, 0)

priority = [[] for _ in range(m + 1)]
for shark_num in range(1, m + 1):
    for _ in range(4):
        priority[shark_num].append(list(map(lambda x : int(x) - 1, input().split())))

smell = [[[0, 0]] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            smell[i][j] = [graph[i][j], cnt]

##
shark_cnt = m
result = 0
while shark_cnt > 1 and result <= 1000:
    org_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(n):
            #if there's shark
            if org_graph[i][j] != 0:
                shark_num = org_graph[i][j]
                moved = False
                # can we move to somewhere else?
                for k in range(4):
                    nx = i + dx[priority[shark_num][dir[shark_num]][k]]
                    ny = j + dy[priority[shark_num][dir[shark_num]][k]]

                    if 0 <= nx < n and  0 <= ny < n:
                        # Yes! we can move!
                        if smell[nx][ny][0] == 0:
                            moved = True
                            graph[i][j] = 0
                            dir[shark_num] = priority[shark_num][dir[shark_num]][k]
                            # is there another shark?
                            if graph[nx][ny] != 0:
                                # i'm first! go away!
                                if graph[nx][ny] > shark_num:
                                    graph[nx][ny] = shark_num
                                shark_cnt -= 1
                            else:
                                graph[nx][ny] = shark_num
                            break
                # No! we don't have any place to move!
                if not moved:
                    # find my smell
                    for k in range(4):
                        nx = i + dx[priority[shark_num][dir[shark_num]][k]]
                        ny = j + dy[priority[shark_num][dir[shark_num]][k]]

                        if 0 <= nx < n and  0 <= ny < n and smell[nx][ny][0] == shark_num:
                            dir[shark_num] = priority[shark_num][dir[shark_num]][k]
                            graph[i][j] = 0
                            graph[nx][ny] = shark_num
                            break

    # remap
    for i in range(n):
        for j in range(n):
            # if there's only smell, -1 left time
            if graph[i][j] == 0:
                if smell[i][j][0] != 0:
                    smell[i][j][1] -= 1
                    if smell[i][j][1] <= 0: smell[i][j] = [0, 0]
            # if there's shark, change smell[][][]
            else:
                smell[i][j] = [graph[i][j], cnt]

    result += 1
if result > 1000: print(-1)
else: print(result)