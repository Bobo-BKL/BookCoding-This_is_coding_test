#n = int(input())

#day = []
#cost = []

#for _ in range(n):
#    d, c = map(int, input().split())
#    day.append(d)
#    cost.append(c)

n = 7
day = [3, 5, 1, 1, 2, 4, 2]
cost = [10, 20, 10, 20, 15, 40, 200]
 
ans = [0] * (n + 1)

max_val = 0
for i in range(n - 1, -1, -1):
    ans[i] = max((cost[i] + ans[i + day[i]]) if (i + day[i] <= n) else max_val, max_val)
    max_val = ans[i]

print(max(ans))