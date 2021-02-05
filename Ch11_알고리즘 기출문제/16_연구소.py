from itertools import combinations
from collections import deque
import copy

#n, m = map(int, input().split())
#graph = []
#for _ in range(n):
#    graph.append(list(map(int, input().split())))

n = 7
m = 7
graph = [
[2, 0, 0, 0, 1, 1, 0],
[0, 0, 1, 0, 1, 2, 0],
[0, 1, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1],
[0, 1, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0]
]


blank = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: blank.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                        
                        if graph[nx][ny] == 0:
                            q. append((nx, ny))
                            graph[nx][ny] = 3
                              
    return graph
    
result = 0
for new_walls in list(combinations(blank, 3)):
    temp_graph = copy.deepcopy(graph)
    
    print(new_walls)
    for wall in new_walls:
        x, y = wall
        temp_graph[x][y] = 1
        
    temp_graph = bfs(temp_graph)
    
    temp_sum = 0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0: temp_sum += 1
            
    result = max(result, temp_sum)
    
print(result)