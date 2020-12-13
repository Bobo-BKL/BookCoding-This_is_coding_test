
n = int(input())

count = 0
for i in range((n + 1) * 60 * 60):
    h = i // 3600
    m = (i - h * 3600) // 60
    s = (i - h * 3600) % 60

    if '3' in str(h) + str(m) + str(s): count += 1

print(count)