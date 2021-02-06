from itertools import combinations

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2: chicken.append((i, j))
        elif board[i][j] == 1: house.append((i, j))
        
comb = list(combinations(chicken, m))

result = 1e9
for chicken in comb:
    sum = 0
    for h in house:
        h_min = 1e9
        h_x, h_y = h
        for c in chicken:
            c_x, c_y = c
            h_min = min(h_min, abs(h_x - c_x) + abs(h_y - c_y))
            
        sum += h_min
        
    result = min(result, sum)
    
print(result)