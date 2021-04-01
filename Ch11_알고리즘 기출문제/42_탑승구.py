G = int(input())
P = int(input())

parent = [i for i in range(G + 1)]
def find(parent, a):
    if a != parent[a]: parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b: parent[b] = a
    else: parent[a] = b

result = 0
go = True
for _ in range(P):
    now = find(parent, int(input()))
    if go:
        if now > 0:
            union(parent, now, now - 1)
            result += 1
        else:
            go = False

print(result)