n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        data[i][j] = data[i][j] + max(data[i - 1][j - 1] if j != 0 else 0, data[i - 1][j] if j != i else 0)
        
result = max(data[n - 1])
print(result)