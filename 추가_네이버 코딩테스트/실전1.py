def solution(A):
    n = len(A)
    dp = [1] * n

    max_val = 1
    for i in range(1, n):
        if A[i - 1] < A[i]:
            dp[i] += dp[i - 1]
            if max_val < dp[i]:
                max_val = dp[i]

    for idx, val in enumerate(dp):
        if val == max_val:
            return idx - val + 1


# [2, 2, 2, 2, 1, 2, -1, 2, 1, 3]
array = [i if i > 1000 else 0 for i in range(150000)]
print(solution(array))
