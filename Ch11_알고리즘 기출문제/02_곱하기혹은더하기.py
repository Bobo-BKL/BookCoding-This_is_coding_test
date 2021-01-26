s = list(map(int, input()))

sum = 0
for num in s:
    if sum <= 1: sum += num
    else: sum *= num
    
print(sum)
