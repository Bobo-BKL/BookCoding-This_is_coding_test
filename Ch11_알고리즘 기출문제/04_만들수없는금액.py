n = int(input())
mon = list(map(int, input().split()))

mon.sort()

target = 1
for m in mon:
    if target < m: break
    target += m
    
print(target)