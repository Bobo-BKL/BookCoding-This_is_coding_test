s = list(input())
s.sort()

sum = 0
for c in s:
    if '0'<= c <= '9':
        sum += int(c)
    else:
        print(c, end='')
        
print(sum)