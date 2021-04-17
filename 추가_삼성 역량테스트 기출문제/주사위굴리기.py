
n, m, x, y, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
instruct = list(map(lambda x: int(x) - 1, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0] * 7

def roll_dice(dir):
    global dice
    if dir == 0: #동
        temp = dice[6]
        dice[6] = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[4]
        dice[4] = temp
    elif dir == 1: #서
        temp = dice[6]
        dice[6] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[3]
        dice[3] = temp
    elif dir == 2: #북
        temp = dice[6]
        dice[6] = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[5]
        dice[5] = temp
    else:  #남
        temp = dice[6]
        dice[6] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[2]
        dice[2] = temp

for inst in instruct:
    nx = x + dx[inst]
    ny = y + dy[inst]

    if 0 <= nx < n and 0 <= ny < m:
        roll_dice(inst)
        print(dice[1])
        if data[nx][ny] == 0:
            data[nx][ny] = dice[6] 
        else:
            dice[6] = data[nx][ny]
            data[nx][ny] = 0

        x, y = nx, ny
