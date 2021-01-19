edges = [
                (29, 1, 2),
                (75, 1, 5),
                (35, 2, 3),
                (34, 2, 6),
                (7, 3, 4),
                (23, 4, 6),
                (13, 4, 7),
                (53, 5, 6),
                (25, 6, 7)
]

parent = [i for i in range(7 + 1)]

def find_parent(parent, x):
    if parent[x] != x: parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b: parent[b] = a
    else: parent[a] = b
    
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)