n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

result = 0
while start <= end:
    mid = (start + end) // 2
    
    sum = 0
    for i in data:
        if i > mid: sum += i - mid
    
    if sum < m: end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)
