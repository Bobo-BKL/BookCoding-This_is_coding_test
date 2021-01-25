food_times = list(map(int, input().split()))
k = int(input())

def next(n):
    return (n + 1) % len(food_times)

now = 0

for _ in range(k + 1):
    if food_times[now] == 0: now = next(now)
    food_times[now] -= 1
    now = next(now)

print(now)