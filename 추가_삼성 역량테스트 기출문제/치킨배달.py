# from itertools import combinations
#
# f = open("C:/Users/wwwbklee/Desktop/치킨배달.txt", 'r')
# lines = f.readlines()
# f.close()
#
# min_val = int(1e9)
#
#
# def calculate_distance(chicken, house):
#     result = 0
#     for h in house:
#         h_x, h_y = h
#         min_h = int(1e9)
#         for chick in chicken:
#             c_x, c_y = chick
#             min_h = min(min_h, abs(h_x - c_x) + abs(h_y - c_y))
#         result += min_h
#     return result
#
#
# line_cnt = 0
# while line_cnt < len(lines):
#     n, m = map(int, (lines[line_cnt]).split()); line_cnt += 1
#     data = []
#     for _ in range(n):
#         data.append(list(map(int, (lines[line_cnt]).split()))); line_cnt += 1
#
#     min_val = int(1e9)
#
#     chickens = []
#     houses = []
#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == 2: chickens.append((i, j))
#             elif data[i][j] == 1: houses.append((i, j))
#
#     for s_chicken in list(combinations(chickens, m)):
#         min_val = min(min_val, calculate_distance(s_chicken, houses))
#
#     print(min_val)
#

from itertools import combinations


def calculate_distance(chicken, house):
    result = 0
    for h in house:
        h_x, h_y = h
        min_h = int(1e9)
        for chick in chicken:
            c_x, c_y = chick
            min_h = min(min_h, abs(h_x - c_x) + abs(h_y - c_y))
        result += min_h
    return result


n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            chickens.append((i, j))
        elif data[i][j] == 1:
            houses.append((i, j))

min_val = int(1e9)
for s_chicken in list(combinations(chickens, m)):
    min_val = min(min_val, calculate_distance(s_chicken, houses))

print(min_val)

