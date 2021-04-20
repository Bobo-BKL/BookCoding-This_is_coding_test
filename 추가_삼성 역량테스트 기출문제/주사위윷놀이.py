from itertools import product

board_in = [
    (13, 16, 19, 25, 30, 35, 40),
    (22, 24, 25, 30, 35, 40),
    (28, 27, 26, 25, 30, 35, 40)
]

# out/in, x, y
dices = list(map(int, input().split()))
result = 0


def get_score(h_nums):
    horses = [[0, -1, -1] for _ in range(4)]
    score = 0
    for i in range(10):
        go = dices[i]
        inout, x, y = horses[h_nums[i]]

        if inout == -2: return 0  # if horse goaled, not available

        if inout > -1:  # out circle
            if 0 < inout < 20 and inout % 5 == 0:  # blue
                nx, ny = inout // 5 - 1, go - 1
                for horse in horses:  # if horse exists, not available
                    if horse[0] == -1:
                        if board_in[nx][ny] == board_in[horse[1]][horse[2]]: return 0
                    elif board_in[nx][ny] == 40 and horse[0] == 20: return 0
                horses[h_nums[i]] = [-1, nx, ny]
                score += board_in[nx][ny]
            else:  # red
                inout += go
                if inout > 20:  # if exceed, goal!
                    horses[h_nums[i]][0] = -2
                else:
                    for horse in horses:  # if horse exists, not available
                        if horse[0] == inout: return 0
                        elif inout == 20 and horse[0] == -1 and board_in[horse[1]][horse[2]] == 40: return 0
                    horses[h_nums[i]][0] = inout
                    score += inout * 2
        else:  # in circle
            nx, ny = x, y + go
            if ny >= len(board_in[nx]):  # if exceed, goal!
                horses[h_nums[i]][0] = -2
            else:
                for horse in horses:  # if horse exists, not available
                    if horse[0] == -1:
                        if board_in[nx][ny] == board_in[horse[1]][horse[2]]: return 0
                    elif board_in[nx][ny] == 40 and horse[0] == 20: return 0
                horses[h_nums[i]] = [-1, nx, ny]
                score += board_in[nx][ny]
    return score


for horse_chosen in list(product([0, 1, 2, 3], repeat=10)):
    result = max(result, get_score(horse_chosen))

print(result)
