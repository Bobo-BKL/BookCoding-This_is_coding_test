import copy
colors = ['w', 'y', 'r', 'o', 'g', 'b']
directions = ['U', 'D', 'F', 'B', 'L', 'R']
n, m = 6, 3

turn_points = [  # face_turn, face_num
    [(0, 0, 0, 0), (2, 4, 3, 5)],
    [(2, 2, 2, 2), (2, 5, 3, 4)],
    [(2, 3, 2, 1), (1, 4, 0, 5)],
    [(0, 3, 0, 1), (1, 5, 0, 4)],
    [(3, 3, 1, 1), (1, 3, 0, 2)],
    [(1, 3, 3, 1), (1, 2, 0, 3)]
]

t = int(input())


def turn_face(face, turn_cnt):
    result = copy.deepcopy(face)
    for _ in range(turn_cnt):
        result = list(zip(*result[::-1]))
    return result


def turn_cube(cube, oface, odir):
    # 기준면 일단 회전!
    cube[oface] = turn_face(cube[oface], odir)

    face_turn_cnts, faces = turn_points[oface]
    # 기준면 중심으로 네 개의 면 복사
    temp = [[] for _ in range(m)]
    for cnt, face in zip(face_turn_cnts, faces):
        temp_add = turn_face(cube[face], cnt)
        for i in range(m):
            temp[i].extend(temp_add[i])

    # 횟수대로 돌려돌려!
    for _ in range(odir):
        s = temp[0][-3:]
        for k in range(3, 0, -1):
            i = m * k - 1
            temp[0][i + 1:i + 4] = temp[0][i - 2:i + 1]
        temp[0][:3] = s

    # 붙여넣기
    col = 0
    for cnt, face in zip(face_turn_cnts, faces):
        temp_add = turn_face([temp[i][col:col + m] for i in range(m)], 4 - cnt)
        for i in range(m):
            cube[face][i] = temp_add[i]
        col += 3


def print_cube_topface(topface):
    for i in range(m):
        print(''.join([colors[element] for element in topface[i]]))


def get_result():
    # test case
    for _ in range(t):
        cube = [[[i] * m for _ in range(m)] for i in range(n)]
        k = int(input())
        cases = list(map(lambda x: (directions.index(x[0]), 3 if x[1] == '-' else 1), input().split()))

        for face_num, dir in cases:
            turn_cube(cube, face_num, dir)

        print_cube_topface(cube[0])


get_result()
