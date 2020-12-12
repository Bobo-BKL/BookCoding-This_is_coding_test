
n = int(input())
plan = input().split()

row = 0
col = 0

for way in plan:
    if way == 'L' and col - 1 >= 0 : col -= 1
    elif  way == 'R' and col + 1 < n : col += 1
    elif  way == 'U' and row - 1 >= 0 : row -= 1
    elif  way == 'D' and row + 1 < n : row += 1
print("목적지:", row + 1, col + 1)
