def solution(A):
    A.sort()
    now = 0
    for elem in A:
        if now + 1 != elem:
            break
        now = elem
    return now + 1


print(solution([2, 3, 1, 5]))