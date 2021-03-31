import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = int(1e9)
result = [INF] * (n + 1)

q = []
heapq.heappush(q, (0, 1))
result[1] = 0

while q:
    now_cost, now = heapq.heappop(q)
    if now_cost > result[now]: continue

    for next in graph[now]:
        next_cost = now_cost + 1
        if next_cost < result[next]:
            result[next] = next_cost
            heapq.heappush(q, (next_cost, next))

minimum = max(result[1:])
target = result.index(minimum) 
count = result.count(minimum)

print(target, minimum, count)