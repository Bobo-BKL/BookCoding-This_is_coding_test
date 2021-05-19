def solution(N):
    cnt = 0
    result = 0
    is_cnt = False
    while N:
        if N % 2:
            if is_cnt:
                result = max(result, cnt)
            cnt = 0
            is_cnt = True
        else:
            cnt = cnt + 1
        N = N // 2

    return result


print(solution(20))
