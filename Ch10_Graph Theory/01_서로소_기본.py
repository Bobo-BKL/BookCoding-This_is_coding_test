parent = [i for i in range(7)]
unions = [(1, 4), (2, 3), (1, 2), (5, 6)]

def find_parent(parent, x):
    if parent[x] != x: return find_parent(parent, parent[x])
    else: return x
    
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b: parent[b] = a
    else: parent[a] = b
    
for union in unions:
    union_parent(parent, union[0], union[1])
    
for p in parent[1:]:
    print(find_parent(parent, p), end = ' ')
    
print()
print(parent[1:])
