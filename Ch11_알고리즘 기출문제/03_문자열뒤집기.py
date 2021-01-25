s = list(map(int, input()))

p = 0
cnt = 0

while p < len(s):
    if s[p] != s[0]:
        cnt += 1
        while s[p] != s[0]: p += 1
    else: p += 1
    
print(cnt)