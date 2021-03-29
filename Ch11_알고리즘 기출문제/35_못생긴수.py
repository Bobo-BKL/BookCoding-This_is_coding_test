n = int(input())

result = [0] * (n)
result[0] = 1
i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    result[i] = min(next2, next3, next5)
    
    if result[i] == next2:
        i2 += 1
        next2 = result[i2] * 2
    if result[i] == next3:
        i3 += 1
        next3 = result[i3] * 3
    if result[i] == next5:
        i5 += 1
        next5 = result[i5] * 5

print(result[n - 1])