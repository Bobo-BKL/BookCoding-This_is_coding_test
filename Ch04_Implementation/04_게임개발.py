row, col = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
been = [[0] * col for _ in range(row)]

x, y, direction = map(int, input().split())
been[x][y] = 1

u_map  = []
for i in range(row):
	u_map.append(list(map(int, input().split())))
	
def turn_left():
	global direction
        direction -= 1
	if direction < 0: direction = 3

result = 1
turn_time = 0

while True:
	turn_left()
	nx = x + dx[direction]
	ny = y + dy[direction]
	
	if 0 <= nx < row and 0 <= ny < col:
		if been[nx][ny] == 0 and u_map[nx][ny] == 0:
			x = nx
			y = ny
			been[x][y] = 1
			turn_time = 0
			result += 1
			continue
		else:
			turn_time += 1
	else:
			turn_time += 1
			
	if turn_time >= 4:
		nx = x - dx[direction]
		ny = y - dy[direction]
		
		if 0 <= nx < row and 0 <= ny < col and u_map[nx][ny] == 0:
			x = nx
			y = ny
			turn_time = 0
		else:
			break;
			
print(result)
