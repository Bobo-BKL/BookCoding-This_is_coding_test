from itertools import combinations

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

def get_status(team):
    sum = 0
    for a, b in list(combinations(team, 2)):
        sum += s[a][b] + s[b][a]
    return sum

min_val = int(1e9)
for start in list(combinations([i for i in range(n)], n // 2)):
    link = [i for i in range(n) if not i in start]
    min_val = min(min_val, abs(get_status(start) - get_status(link)))

print(min_val)