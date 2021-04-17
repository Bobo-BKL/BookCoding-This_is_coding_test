
# f = open("C:/Users/wwwbklee/Desktop/드래곤커브.txt", 'r')
# lines = f.readlines()
# f.close()
#
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
#
#
# def draw_dragon(graph, drag):
#     start_x, start_y, di, g = drag
#
#     dirs = [di]
#     graph[start_x][start_y] = True
#     for _ in range(g):
#         temp = []
#         for i in range(len(dirs)):
#             temp.append((dirs[-i - 1] + 1) % 4)
#         dirs.extend(temp)
#
#     for d in dirs:
#         start_x += dx[d]
#         start_y += dy[d]
#         if 0 <= start_x <= 100 and 0 <= start_y <= 100:
#             graph[start_x][start_y] = True
#
#     return graph
#
#
# def count_boxes(graph):
#     result = 0
#     for i in range(100):
#         for j in range(100):
#             if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
#                 result += 1
#     return result
#
#
# line_cnt = 0
# while line_cnt < len(lines):
#     n = int(lines[line_cnt])
#     line_cnt += 1
#     dragons = []
#     for _ in range(n):
#         y, x, direct, gen = map(int, (lines[line_cnt]).split())
#         dragons.append((x, y, direct, gen))
#         line_cnt += 1
#
#     # main
#     data = [[False] * 101 for _ in range(101)]
#     for dragon in dragons:
#         data = draw_dragon(data, dragon)
#
#     print(count_boxes(data))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def draw_dragon(graph, drag):
    start_x, start_y, di, g = drag

    dirs = [di]
    graph[start_x][start_y] = True
    for _ in range(g):
        temp = []
        for i in range(len(dirs)):
            temp.append((dirs[-i - 1] + 1) % 4)
        dirs.extend(temp)

    for d in dirs:
        start_x += dx[d]
        start_y += dy[d]
        if 0 <= start_x <= 100 and 0 <= start_y <= 100:
            graph[start_x][start_y] = True

    return graph


def count_boxes(graph):
    result = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
                result += 1
    return result


n = int(input())
dragons = []
for _ in range(n):
    y, x, direct, gen = map(int, input().split())
    dragons.append((x, y, direct, gen))

# main
data = [[False] * 101 for _ in range(101)]
for dragon in dragons:
    data = draw_dragon(data, dragon)

print(count_boxes(data))
