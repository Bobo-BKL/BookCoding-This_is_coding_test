#n = int(input())
#data = list(map(int, input().split()))

n=7
data = [15, 11, 4, 8, 5, 2, 4]

result = [1] * (n)

data.reverse()

for i in range(1, n):
    for j in range(i):
        if data[j] < data[i]:
            result[i] = max(result[i], result[j] + 1)

print(n - max(result))