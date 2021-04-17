# import copy
#
# f = open("C:/Users/wwwbklee/Desktop/사다리조작.txt", 'r')
# lines = f.readlines()
# f.close()
#
# line_num = 0
# result = int(1e9)
#
#
# def is_one_goal(graph, num, row):
#     x, y = 1, num
#     while x <= row:
#         y = y + graph[x][y]
#         x += 1
#     if y == num: return True
#     else: return False
#
#
# def check_all_goal(graph, row, col):
#     for i in range(1, col + 1):
#         if not is_one_goal(graph, i, row): return False
#     return True
#
#
# def recurr_ladder(graph, cnt, added, row, col):
#     global result
#     if added > 3: return
#
#     if check_all_goal(graph, row, col):
#         result = min(result, added)
#         return
#
#     while cnt <= (row + 1) * (col + 1):
#         x, y = cnt // col, cnt % col
#         if 1 <= x <= row and 1 <= y <= col:
#             if graph[x][y] == 0 and y + 1 <= col and graph[x][y + 1] == 0:
#                 array = copy.deepcopy(graph)
#                 array[x][y], array[x][y + 1] = 1, -1
#                 recurr_ladder(array, cnt + 1, added + 1, row, col)
#         cnt += 1
#
#
# while line_num < len(lines):
#     m, l, n = map(int, (lines[line_num]).split()); line_num += 1
#     data = [[0] * (m + 1) for _ in range(n + 1)]
#     for _ in range(l):
#         a, b = map(int, (lines[line_num]).split()); line_num += 1
#         data[a][b] = 1
#         data[a][b + 1] = -1
#
#     # main문 들어간다잉~
#     result = int(1e9)
#     recurr_ladder(data, 0, 0, n, m)
#     print(result) if result < int(1e9) else print(-1)


result = int(1e9)


def is_one_goal(graph, num, row):
    x, y = 1, num
    while x <= row:
        y = y + graph[x][y]
        x += 1
    if y == num: return True
    else: return False


def check_all_goal(graph, row, col):
    for i in range(1, col + 1):
        if not is_one_goal(graph, i, row): return False
    return True


def recurr_ladder(graph, cnt, added, row, col):
    global result
    if added > 3: return

    if check_all_goal(graph, row, col):
        result = min(result, added)
        return
    if added == 3: return

    while cnt <= (row + 1) * (col + 1):
        x, y = cnt // (col + 1), cnt % (col + 1)
        if 1 <= x <= row and 1 <= y <= col:
            if y + 1 <= col and graph[x][y] == 0 and graph[x][y + 1] == 0:
                graph[x][y], graph[x][y + 1] = 1, -1
                recurr_ladder(graph, cnt + 1, added + 1, row, col)
                graph[x][y], graph[x][y + 1] = 0, 0
        cnt += 1


m, l, n = map(int, input().split())
data = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(l):
    a, b = map(int, input().split())
    data[a][b] = 1
    data[a][b + 1] = -1

recurr_ladder(data, m + 2, 0, n, m)
print(result) if result < int(1e9) else print(-1)
