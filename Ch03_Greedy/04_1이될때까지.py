
n, k = map(int, input().split())

result = 0
while n is not 1:
    if int(n % k) is 0: n //= k
    else: n -= 1
    result += 1
print("결과:", result)