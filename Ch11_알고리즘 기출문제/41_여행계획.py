n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visitings = list(map(lambda a : int(a) - 1, input().split()))

parent = [i for i in range(n)]

def find(a):
    if a != parent[a]: parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b: parent[b] = a
    else: parent[a] = b

for i in range(n):
    for j in range(i):
        if graph[i][j]:
            union(i, j)

result = 'YES'
for i in range(1, m):
    a = visitings[i - 1]
    b = visitings[i]

    if find(a) != find(b):
        result = 'NO'
        break

print(result)