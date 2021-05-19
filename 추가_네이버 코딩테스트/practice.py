from itertools import permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from collections import deque, Counter
import heapq
import copy


INF = int(1e9)

############################
array = [i for i in range(20) if i % 2 == 1]
array2 = [[0] * 3 for _ in range(3)]


print((lambda a, b: a + b)(2, 3))


users = [{'email': 'wwwbklee@naver.com', 'name': '이보경'},
         {'email': 'drop5656@naver.com', 'name': '신승환'}]
print(list(map(lambda user: user['email'], users)))


a = {1, 6, 4, 4, 2, 8, 1, 15}
print(a)
b = {'a', 'c', 'v', 'c', 'a', 'b', 'b', 'z', 'A'}
print(b)
print(a | b)


data = [1, 2, 4, 4, 6]
print(list(permutations(data, 5)))
print(list(combinations(data, 5)))
print(list(product(data, repeat=5)))
print(list(combinations_with_replacement(data, 5)))


print(bisect_right(data, 4) - bisect_left(data, 4))


q = deque(data)
q.append(144)
q.popleft()
print(list(q))
q.rotate(1)
print(list(q))


counter = Counter(['red', 'blue', 'red', 'purple'])
print(counter['blue'])


print(chr(ord('A')))


print(''.join(['red', 'blue', 'red']))


heapq.heapify(data)
heapq.heappop(data)
heapq.heappush(data, 4)
print(data)


data = [[0, 5, 0], [2, 1, 5], [1, 9, 9], [7, 6, 0]]
def sort_array(d): return d[1]
print(sorted(data, key=sort_array))
print(sorted(data, key=lambda d: d[1]))


############################
graph = [
    [1],
    [1, 2],
    [0]
]
cnt_graph = 3


def bfs(graph, n, start):
    visited = [False] * n
    q = deque([start])
    visited[start] = True
    result = [start]

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                result.append(next)
    return result


def dfs(graph, n, start):
    result = []
    visited = [False] * n

    def DFS(now):
        nonlocal result
        visited[now] = True
        result.append(now)
        for next in graph[now]:
            if not visited[next]:
                DFS(next)

    DFS(start)
    return result


print(bfs(graph, cnt_graph, 1))
print(dfs(graph, cnt_graph, 1))


############################
graph = [
    [(10, 1)],
    [(5, 2)],
    [(20, 0), (1, 3)],
    []
]
cnt_graph = 4


def dijkstra(graph, cnt_graph, start):
    q = []
    distances = [INF] * cnt_graph

    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        now_dist, now = heapq.heappop(q)
        if distances[now] < now_dist: continue

        for next_dist, next in graph[now]:
            cost = now_dist + next_dist
            if cost < distances[next]:
                distances[next] = cost
                heapq.heappush(q, (cost, next))

    return distances


print(dijkstra(graph, cnt_graph, 0))


def floyd_warshall(graph, cnt_graph):
    for k in range(cnt_graph):
        for i in range(cnt_graph):
            for j in range(cnt_graph):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


############################
def find(parent, a):
    if a != parent[a]: parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b: parent[b] = a
    else: parent[a] = b


def cycle(parent, a, b):
    if find(parent, a) == find(parent, b):
        return True
    else: return False


def kruskal(parent, edges):
    result = 0

    edges.sort()
    for cost, a, b in edges:
        if not cycle(parent, a, b):
            union(parent, a, b)
            result += cost

    return result


############################
def topology_sort(graph, indegree):
    result = []
    q = deque()

    for idx, cnt in enumerate(indegree):
        if cnt == 0:
            q.append(idx)

    while q:
        now = q.popleft()
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    return result


############################
def rotate_2d_clockwise(array):
    return list(zip(*array[::-1]))


def rotate_2d_anticlockwise(array):
    return list(zip(*array))[::-1]


def rotate_1d(array, n):
    return array[-n:] + array[:-n]


def get_col(array, n):
    return list(zip(*array))[n]


array = [
    [1, 2],
    [3, 4]
]

print(array[::-1])
print(rotate_2d_clockwise(array))
