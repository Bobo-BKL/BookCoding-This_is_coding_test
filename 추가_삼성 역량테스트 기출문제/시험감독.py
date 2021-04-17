
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = n
for test in a:
    test -= b

    if test < 1: continue

    if test % c != 0:
        result += test // c + 1
    else: result += test // c

print(result)