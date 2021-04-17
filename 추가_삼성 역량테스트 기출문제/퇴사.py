
n = int(input())

t = [0] * (n + 1)
p = [0] * (n + 1)
dp = [0] * (n + 2)
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

if t[n] <= 1: dp[n] = p[n]
for i in range(n - 1, 0, -1):
    if t[i] + i - 1 > n: dp[i] = dp[i + 1]
    else: dp[i] = max(dp[i + 1], dp[t[i] + i] + p[i])

print(dp[1])