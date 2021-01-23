n = int(input())
data = list(map(int, input().split()))

data.sort(reverse = True)

now = 0
g = 0
while  now < n:
    now += data[now]
    g += 1
    
print(g)
