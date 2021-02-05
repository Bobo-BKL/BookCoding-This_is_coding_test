from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    v = q.popleft()
    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            q.append(i)

check = False        
for i in range(1, n + 1):
    if distance[i] == k: print(i)
    check = True
    
if not check: print(-1)
    