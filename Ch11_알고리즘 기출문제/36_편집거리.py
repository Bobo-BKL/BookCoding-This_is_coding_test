str1 = input()
str2 = input()

n = len(str1)
m = len(str2)

result = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    result[i][0] = i
for i in range(m + 1):
    result[0][i] = i

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]: result[i][j] = result[i - 1][j - 1]
        else:
            result[i][j] = 1 + min(result[i-1][j-1], result[i][j-1], result[i-1][j])
print(result[n][m])
