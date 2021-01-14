store = [0] * 1000000

n = int(input())
for i in list(map(int, input().split())):
    store[i] = 1
    
m = int(input())
for i in list(map(int, input().split())):
    if store[i] == 1: print('yes', end=' ')
    else: print('no', end = ' ')