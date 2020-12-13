data = input()
row = int(data[1]) - 1
col = int(ord(data[0])) - int(ord('a'))

steps = [ (-2, -1), (-1, -2), (1, -2), (-2, 1), (-1, 2), (2, -1), (1, 2), (2, 1) ]

result = 0
for step in steps:
    tmp_row = row + step[0]
    tmp_col = col + step[1]

    if tmp_row >= 0 and tmp_row < 8 and tmp_col >= 0 and tmp_col < 8:
        result += 1

print(result)