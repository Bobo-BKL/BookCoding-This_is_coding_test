n = int(input())
store = set(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

for item in find:
    if item in store: print('yes', end = ' ')
    else: print('no', end = ' ')