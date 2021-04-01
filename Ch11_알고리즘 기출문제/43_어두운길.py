
n,m = map(int, input().split())

edges = []
parent = [i for i in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

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

edges.sort()
result = 0
for edge in edges:
    cost, x, y = edge

    if not cycle(parent, x, y):
        union(parent, x, y)
    else: result += cost

print(result)