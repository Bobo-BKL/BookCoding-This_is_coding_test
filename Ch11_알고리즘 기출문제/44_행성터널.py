n = int(input())

x = []
y = []
z = []
for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = []
for a in range(1, n):
    edges.append((x[a][0] - x[a - 1][0], x[a - 1][1], x[a][1]))
    edges.append((y[a][0] - y[a - 1][0], y[a - 1][1], y[a][1]))
    edges.append((z[a][0] - z[a - 1][0], z[a - 1][1], z[a][1]))

parent = [i for i in range(n)]
def find(parent, a):
    if parent[a] != a: parent[a] = find(parent, parent[a])
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

result = 0
edges.sort()
for edge in edges:
    cost, x, y = edge

    if not cycle(parent, x, y):
        result += cost
        union(parent, x, y)

print(result)