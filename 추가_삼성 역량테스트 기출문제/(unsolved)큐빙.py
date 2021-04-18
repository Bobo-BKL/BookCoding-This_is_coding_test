# 해당 코드의 문제
# 면 자체의 고정된 방향때문에 각 상황에서의 line 대입 시 장애가 생김

colors = ['w', 'y', 'r', 'o', 'g', 'b']
faces = ['U', 'D', 'F', 'B', 'L', 'R']
directions = ['+', '-']
turns = [
    # [딸린 4개의 면번호 시계 방향순]
    [2, 4, 3, 5],
    [2, 5, 3, 4],
    [0, 5, 1, 4],
    [0, 4, 1, 5],
    [0, 2, 1, 3],
    [0, 3, 1, 2]
]
match_rowcol = [
    # [행0인가 열1인가, 그것의 번호(, 인덱싱 방향?)]
    [[0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 2], [0, 2], [0, 2], [0, 2]],
    [[0, 2], [1, 0], [0, 2], [1, 2]],
    [[0, 0], [1, 0], [0, 0], [1, 2]],
    [[1, 0], [1, 0], [1, 0], [1, 2]],
    [[1, 2], [1, 0], [1, 2], [1, 2]]
]


# 해당면을 돌려
def turn_current_face(top_face, di):
    temp = [[0] * 3 for _ in range(3)]
    if di == 0:  # 시계방향
        for i in range(3):
            for j in range(3):
                temp[j][3 - i - 1] = top_face[i][j]
    else:  # 반시계방향
        for j in range(3):
            for i in range(3):
                temp[i][j] = top_face[j][3 - i - 1]
    return temp


def get_col(fa, num):
    return [fa[i][num] for i in range(3)]


def get_row(fa, num):
    return fa[num]


def get_rowcol(is_rowcol, turn_face, num):
    if is_rowcol == 0:  #행
        return get_row(turn_face, num)
    else:
        return get_col(turn_face, num)


# !!!!!고칠거면 여길 좀 어떻게 고쳐봐!!!!!
# line의 인덱스랑 면의 인덱스 방향이 일치한지 또 생각해줘야함
def change_one_line(is_rowcol, face_a, line, num):
    if is_rowcol == 0:  # 행
        face_a[num] = line
    else:  # 열
        for i in range(3):
            face_a[i][num] = line[i]
    return face_a


def turn_clockwise_affected_face(cu, fa):
    faces_to_turn = turns[fa]

    saved = get_rowcol(match_rowcol[fa][3][0], cu[faces_to_turn[3]], match_rowcol[fa][3][1])
    for f in range(3, 0, -1):
        temp = get_rowcol(match_rowcol[fa][f - 1][0], cu[faces_to_turn[f - 1]], match_rowcol[fa][f - 1][1])
        cu[faces_to_turn[f]] = change_one_line(match_rowcol[fa][f][0], cu[faces_to_turn[f]], temp, match_rowcol[fa][f][1])

    cu[faces_to_turn[0]] = change_one_line(match_rowcol[fa][0][0], cu[faces_to_turn[0]], saved, match_rowcol[fa][0][1])
    return cu


def turn_counterclockwise_affected_face(cu, fa):
    faces_to_turn = turns[fa]

    saved = get_rowcol(match_rowcol[fa][0][0], cu[faces_to_turn[0]], match_rowcol[fa][0][1])
    for f in range(1, 4):
        temp = get_rowcol(match_rowcol[fa][f][0], cu[faces_to_turn[f]], match_rowcol[fa][f][1])
        cu[faces_to_turn[f - 1]] = change_one_line(match_rowcol[fa][f - 1][0], cu[faces_to_turn[f - 1]], temp, match_rowcol[fa][f - 1][1])

    cu[faces_to_turn[3]] = change_one_line(match_rowcol[fa][3][0], cu[faces_to_turn[3]], saved, match_rowcol[fa][3][1])
    return cu


# 해당면에 딸린 네놈 돌려
def turn_all_affected_face(cu, fa, di):
    if di == 0:  # 시계방향
        cu = turn_clockwise_affected_face(cu, fa)
    else:  # 반시계방향
        cu = turn_counterclockwise_affected_face(cu, fa)
    return cu


def print_top_face(top_face):
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(colors[top_face[i][j]])
        print(''.join(temp))


T = int(input())
for _ in range(T):
    # init cube
    cube = [[] for _ in range(6)]
    for c in range(6):
        for _ in range(3):
            cube[c].append([c] * 3)

    n = int(input())
    data = list(input().split())

    for c in range(n):
        face, direct = data[c]
        face = faces.index(face)
        direct = directions.index(direct)

        # main
        cube[face] = turn_current_face(cube[face], direct)
        cube = turn_all_affected_face(cube, face, direct)

    print_top_face(cube[0])

