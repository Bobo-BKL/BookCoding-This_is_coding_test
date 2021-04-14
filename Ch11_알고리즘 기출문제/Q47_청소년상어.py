import copy
n = 4
INF = 9
EMPTY = 0
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))

    for j in range(0, n * 2, 2):
        cost = data[j]
        dir = data[j + 1]
        graph[i].append([cost, dir - 1])

##
def shark_find_fish(graph, teen_shark_x, teen_shark_y):
    teen_shark_dir = graph[teen_shark_x][teen_shark_y][1]
    x, y = teen_shark_x + dx[teen_shark_dir], teen_shark_y + dy[teen_shark_dir]
    fishes = []
    while 0 <= x < n and 0 <= y < n:
        if graph[x][y][0] != EMPTY: fishes.append((x, y))
        x, y = x + dx[teen_shark_dir], y + dy[teen_shark_dir]

    return fishes

# None: no fish like 'fish_num'
# fish returned: found fish_num and returned
def fish_find_next_smallest(graph, fish_num):
    for i in range(n):
        for j in range(n):
            if fish_num == graph[i][j][0]:
                return (i, j)
    return None

# swap if fish can move
def fish_move(graph, teen_shark_x, teen_shark_y):
    for i in range(1, 17):
        fish = fish_find_next_smallest(graph, i)
        if not fish: continue

        fish_x, fish_y = fish
        fish_dir = graph[fish_x][fish_y][1]

        for i in range(1, INF):
            nx = fish_x + dx[fish_dir]
            ny = fish_y + dy[fish_dir]

            if 0 <= nx < n and 0 <= ny < n and not (nx == teen_shark_x and ny == teen_shark_y):
                graph[fish_x][fish_y][1] = fish_dir
                graph[fish_x][fish_y], graph[nx][ny] = graph[nx][ny], graph[fish_x][fish_y]
                break
            else:
                fish_dir = (fish_dir + 1) % (INF - 1)


##
result = 0
def dfs(graph, teen_shark_x, teen_shark_y, total):
    global result
    graph = copy.deepcopy(graph)
    
    total += graph[teen_shark_x][teen_shark_y][0]
    graph[teen_shark_x][teen_shark_y][0]= EMPTY

    # fish movement
    fish_move(graph, teen_shark_x, teen_shark_y)

    # shark find biggest fish
    fishes = shark_find_fish(graph, teen_shark_x, teen_shark_y)
    if len(fishes) == 0:
        result = max(result, total)
        return

    for fish_x, fish_y in fishes:
        dfs(graph, fish_x, fish_y, total)

dfs(graph, 0, 0, 0)
print(result)