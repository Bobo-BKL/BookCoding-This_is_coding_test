from collections import deque
import copy

n = int(input())

graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    subject = list(map(int, input().split()))
    
    time[i] = subject[0]
    for x in subject[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

result = copy.deepcopy(time)
q = deque()

for i in range(len(indegree[1:])):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    now = q.popleft()
    
    for i in graph[now]:
        result[i] = max(result[i], result[now] + time[i])
        indegree[i] -= 1
        if indegree[i] == 0: q.append(i)
        
for i in range(1, n + 1):
    print(result[i])