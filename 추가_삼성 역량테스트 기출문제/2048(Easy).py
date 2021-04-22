from collections import deque
import copy
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def find_biggest(data):
    result = 0
    for i in range(n):
        result = max(result, max(data[i]))
    return result


def regard_multi(data):
    if len(data) == 1: return deque([data[0]])

    q = deque()
    head = 1
    while True:
        if data[head - 1] == data[head]:
            q.append(data[head - 1] * 2)
            if head + 2 == len(data):
                q.append(data[head + 1])
                break
            elif head + 2 > len(data):
                break
            head += 2
        else:
            q.append(data[head - 1])
            if head + 1 == len(data):
                q.append(data[head])
                break
            head += 1

    return q


def merge_together(graph, dir):
    result = [[0] * n for _ in range(n)]
    # 위쪽
    if dir == 0:
        for j in range(n):
            # 배열로 넣어
            temps = []
            for i in range(n):
                if graph[i][j] != 0: temps.append(graph[i][j])
            if len(temps) <= 0: continue
            # 큐로 합병해
            q = regard_multi(temps)
            # 큐를 result 로 넣어
            for i in range(n):
                if q: result[i][j] = q.popleft()
                else: result[i][j] = 0
    # 오른쪽
    elif dir == 1:
        for i in range(n):
            # 배열로 넣어
            temps = []
            for j in range(1, n + 1):
                if graph[i][-j] != 0: temps.append(graph[i][-j])
            if len(temps) <= 0: continue
            # 큐로 합병해
            q = regard_multi(temps)
            # 큐를 result 로 넣어
            for j in range(1, n + 1):
                if q:
                    result[i][-j] = q.popleft()
                else:
                    result[i][-j] = 0
    # 아래
    elif dir == 2:
        for j in range(n):
            # 배열로 넣어
            temps = []
            for i in range(1, n + 1):
                if graph[-i][j] != 0: temps.append(graph[-i][j])
            if len(temps) <= 0: continue
            # 큐로 합병해
            q = regard_multi(temps)
            # 큐를 result 로 넣어
            for i in range(1, n + 1):
                if q:
                    result[-i][j] = q.popleft()
                else:
                    result[-i][j] = 0
    # 왼쪽
    elif dir == 3:
        for i in range(n):
            # 배열로 넣어
            temps = []
            for j in range(n):
                if graph[i][j] != 0: temps.append(graph[i][j])
            if len(temps) <= 0: continue
            # 큐로 합병해
            q = regard_multi(temps)
            # 큐를 result 로 넣어
            for j in range(n):
                if q:
                    result[i][j] = q.popleft()
                else:
                    result[i][j] = 0

    return result


def bfs():
    result = 0
    q = deque([(board, 0)])

    while q:
        original_graph, count = q.popleft()

        # 다섯번째까지 오면 그만
        if count == 5:
            result = max(result, find_biggest(original_graph))
            continue

        for dir in range(4):
            copied_graph = merge_together(copy.deepcopy(original_graph), dir)
            q.append((copied_graph, count + 1))

    return result


print(bfs())