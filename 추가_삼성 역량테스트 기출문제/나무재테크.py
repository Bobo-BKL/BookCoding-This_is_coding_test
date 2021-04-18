from collections import deque

n, m, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

trees = {(i, j): deque() for i in range(1, n + 1) for j in range(1, n + 1)}  # {(x, y): age}
for _ in range(m):
    x, y, age = map(int, input().split())
    trees[(x, y)].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

foods = [[5] * (n + 1) for _ in range(n + 1)]


def spring_and_summer():
    global trees, foods
    for (tree_x, tree_y), tree_ages in trees.items():
        if len(tree_ages) == 0: continue
        trees_survived = deque()
        sums = 0
        for tree_age in tree_ages:
            # 봄입니다
            if foods[tree_x][tree_y] >= tree_age:
                foods[tree_x][tree_y] -= tree_age
                trees_survived.append(tree_age + 1)
            else:
                sums += tree_age // 2
        trees[(tree_x, tree_y)] = trees_survived

        # 여름입니다
        foods[tree_x][tree_y] += sums


def autumn():
    global trees
    for (tree_x, tree_y), tree_ages in trees.items():
        for tree_age in tree_ages:
            if tree_age % 5 != 0: continue
            for di in range(8):
                nx, ny = tree_x + dx[di], tree_y + dy[di]
                if 1 <= nx <= n and 1 <= ny <= n:
                    trees[(nx, ny)].appendleft(1)


def winter():
    global foods
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            foods[i][j] += A[i - 1][j - 1]


for _ in range(k):
    spring_and_summer()
    autumn()
    winter()

result = 0
for tree in trees.values():
    result += len(tree)
print(result)
