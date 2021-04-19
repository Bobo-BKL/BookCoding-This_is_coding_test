n = int(input())

people = []
for _ in range(n):
    people.append(list(map(int, input().split())))


def set_bounds(graph, x, y, d1, d2):
    # set 5
    temps = [set([]) for _ in range(n)]
    for i in range(d1 + 1):
        graph[x + i][y - i] = graph[x + d2 + i][y + d2 - i] = 5
        temps[x + i].add(y - i)
        temps[x + d2 + i].add(y + d2 - i)
    for j in range(d2 + 1):
        graph[x + j][y + j] = graph[x + d1 + j][y - d1 + j] = 5
        temps[x + j].add(y + j)
        temps[x + d1 + j].add(y - d1 + j)
    for row in range(n):
        if len(temps[row]) <= 1: continue
        for col in range(min(temps[row]) + 1, max(temps[row])):
            graph[row][col] = 5

    # set 1
    for i in range(x + d1):
        for j in range(y + 1):
            if not graph[i][j]: graph[i][j] = 1

    # set 2
    for i in range(x + d2 + 1):
        for j in range(y + 1, n):
            if not graph[i][j]: graph[i][j] = 2

    # set 3
    for i in range(x + d1, n):
        for j in range(y - d1 + d2):
            if not graph[i][j]: graph[i][j] = 3

    # set 4
    for i in range(x + d2 + 1, n):
        for j in range(y - d1 + d2, n):
            if not graph[i][j]: graph[i][j] = 4

    return graph


def count_bounds(graph):
    boundary = [0] * 5
    for i in range(n):
        for j in range(n):
            boundary[graph[i][j] - 1] += people[i][j]
    return boundary


def cal_minimum_val():
    result = int(1e9)
    for row in range(n):
        for col in range(n):

            for d1 in range(1, col + 1):
                for d2 in range(1, n - col):
                    if not (1 <= d1 + d2 < n - row): continue

                    graph = [[0] * n for _ in range(n)]

                    graph = set_bounds(graph, row, col, d1, d2)
                    boundary = count_bounds(graph)

                    result = min(result, max(boundary) - min(boundary))
                    if result == 0: return 0

    return result


print(cal_minimum_val())