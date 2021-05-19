from collections import deque


def solution(A, K):
    q = deque(A)
    q.rotate(K)
    return list(q)


print(solution([3, 8, 9, 7, 6], 3))
