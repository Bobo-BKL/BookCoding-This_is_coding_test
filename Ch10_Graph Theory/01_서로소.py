parent = [i for i in range(7)]
unions = [(1, 4), (2, 3), (1, 2), (5, 6)] # [(1, 2), (1, 3), (2, 3)]
cycle = False
def find_parent(parent, x):
    if parent[x] != x: 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b: parent[b] = a
    else: parent[a] = b
    
for union in unions:
    union_parent(parent, union[0], union[1])
    if find_parent(parent, union[0]) == find_parent(parent, union[1]): cycle = True
    
for p in parent[1:]:
    print(find_parent(parent, p), end = ' ')
    
print()
print(parent[1:])
print('사이클:', cycle)
