n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find_parent(parent, x):
    if parent[x] != x: parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    
edges.sort()

last = 0
result = 0
for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
        
print(result - last)