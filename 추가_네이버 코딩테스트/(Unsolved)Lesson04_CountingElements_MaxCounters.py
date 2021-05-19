def solution(N, A):
    result = [0] * N
    Max = 0
    for X in A:
        if X <= N:
            result[X - 1] += 1
            Max = max(Max, result[X - 1])
        else:
            result = [Max] * N

    return result


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
