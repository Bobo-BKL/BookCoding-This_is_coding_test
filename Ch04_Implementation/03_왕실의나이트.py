data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

steps = [
			(-2, -1), (-1, -2), (1, -2), (-2, 1),
			(2, 1), (1, 2), (-1, 2), (2, -1)
]

result = 0

for step in steps:
	next_r = step[0] + row
	next_c = step[1] + col
	
	if 0 < next_r < 9 and 0 < next_c < 9: result += 1

print(result)
