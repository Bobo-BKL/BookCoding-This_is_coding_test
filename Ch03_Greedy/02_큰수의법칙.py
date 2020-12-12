n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

first_cnt = m // (k + 1) * k + m % (k + 1)
second_cnt = m - first_cnt

result = first * first_cnt + second * second_cnt
print("결과:", result)