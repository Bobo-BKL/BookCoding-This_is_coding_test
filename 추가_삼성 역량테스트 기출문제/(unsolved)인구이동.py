# 80%에서 시간초과 뜸
# 해당 코드는 그래프로 작성됨
# bfs로 작성하는게 시간단축이 더 되는 듯

n, r, l = map(int, input().split())

people = []
for _ in range(n):
    dl = list(map(int, input().split()))
    for d in dl:
        people.append(d)

dx = [0, 1]
dy = [1, 0]


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b: parent[b] = a
    else: parent[a] = b


def is_cycle(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        return True
    else: return False


# 여기를 단축시킬 방법을 찾아야함
def connect_cities(parent):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                a, b = i * n + j, nx * n + ny
                if 0 <= nx < n and 0 <= ny < n:
                    if r <= abs(people[a] - people[b]) <= l:
                        count += 1
                        union_parent(parent, a, b)

    if count == 0: return False
    else: return True


def start_people_move(parent):
    global people
    groups = set(parent)
    for city in groups:
        sums = 0
        linked_cities = []

        for i in range(n * n):
            if city == find_parent(parent, i):
                linked_cities.append(i)
                sums += people[i]

        if len(linked_cities) <= 1: continue

        distributed = sums // len(linked_cities)
        for i in linked_cities:
            people[i] = distributed


result = 0
while True:
    parents = [i for i in range(n * n)]
    if not connect_cities(parents): break
    start_people_move(parents)
    result += 1

print(result)