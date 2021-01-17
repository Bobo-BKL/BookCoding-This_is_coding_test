import heapq

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

distance = [INF] * len(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

print(distance[1:])        