from collections import deque


def solution(n, path, order):
    answer = True

    graph = [[] for _ in range(n)]
    q = deque()
    for a, b in path:
        if a == 0:
            q.append(b)
            graph[0].append(b)
        if b == 0:
            q.append(a)
            graph[0].append(a)

    while q:
        node = q.popleft()
        for a, b in path:
            if a == node:
                if node not in graph[b]:
                    q.append(b)
                    graph[node].append(b)
            if b == node:
                if node not in graph[a]:
                    q.append(a)
                    graph[node].append(a)

    # 자, 봐봐.. (DoorB, KeyA) (DoorA, KeyB) 이런 관계가 있으면 False야!
    for keyA, doorA in order:
        for doorB in range(n):
            if keyA in graph[doorB]:
                for keyB, tempB in order:
                    if doorB == tempB:
                        if keyB in graph[doorA]:
                            return False
                        break
                break

    return answer

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))
