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

def find_cycle(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        return 'YES'
    else: return 'NO'

result = []
for _ in range(m):
    action, a, b = map(int, input().split())
    
    if action == 0:
        union_parent(parent, a, b)
    else:
        result.append(find_cycle(parent, a, b))
        
for i in range(len(result)): print(result[i])