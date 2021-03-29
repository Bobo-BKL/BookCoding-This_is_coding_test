n, m = map(int, input().split())
data = list(map(int, input().split()))

dp = []
index = 0
for i in range(n):
    dp.append(data[index:index + m])
    index += m

for j in range(1, m):
    for i in range(n):
        l_up = l_dwn = 0
        if i != 0: l_up = dp[i][j] + dp[i - 1][j - 1]
        if i != (n - 1): l_dwn = dp[i][j] + dp[i + 1][j - 1]
        l = dp[i][j] + dp[i][j - 1]

        dp[i][j] = max(l_up, l_dwn, l)

result = 0
for i in range(n):
    result = max(result, dp[i][m - 1])
print(result)