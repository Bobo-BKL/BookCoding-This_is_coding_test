from collections import deque

input = [
                (1, 2),
                (1, 5),
                (2, 3),
                (2, 6),
                (3, 4),
                (4, 7),
                (5, 6),
                (6, 4)
]

graph = [[] for _ in range(8)]
indegree = [0] * len(graph)

for data in input:
    graph[data[0]].append(data[1])
    indegree[data[1]] += 1
    
result = []
def topology_sort():
    q = deque()
    
    for i in range(1, len(graph)):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        result.append(node)
        
        for child in graph[node]:
            indegree[child] -= 1
            if indegree[child] == 0: q.append(child)
            
topology_sort()
print(result)