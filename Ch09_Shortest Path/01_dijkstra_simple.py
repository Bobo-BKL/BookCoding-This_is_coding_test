INF = int(1e9)

# graph = [[] for i in range(n + 1)]
graph = [
                [],
                [(2, 2), (3, 5), (4, 1)],
                [(3, 3), (4, 2)],
                [(2, 3), (6, 5)],
                [(3, 3), (5, 1)],
                [(3, 1), (6, 2)],
                []
]

visited = [False] * (len(graph))
distance = [INF] * (len(graph))

def get_small_node():
    min_val = INF
    index = 0
    for i in range(1, len(graph)):
        if distance[i] < min_val and not visited[i]:
            index = i
            min_value = distance[i]
            
    return index
    
def dijkstra(next):
    distance[next] = 0
        
    for _ in range(len(graph) - 1):
        next = get_small_node()
        visited[next] = True
        
        for node in graph[next]:
            distance[node[0]] = min(distance[next] + node[1], distance[node[0]])
            
dijkstra(1)

print(distance[1:])
