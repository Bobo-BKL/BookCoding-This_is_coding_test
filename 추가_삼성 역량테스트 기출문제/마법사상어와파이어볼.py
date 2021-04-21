import heapq

n, f, k = map(int, input().split())
fireballs = []
for _ in range(f):
    li = list(map(int, input().split()))
    li[0] -= 1
    li[1] -= 1
    fireballs.append(li)
heapq.heapify(fireballs)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def move_fireball():
    global fireballs

    q = []
    while fireballs:
        r, c, m, s, d = heapq.heappop(fireballs)
        nx, ny = (r + dx[d] * s) % n, (c + dy[d] * s) % n
        heapq.heappush(q, [nx, ny, m, s, d])

    fireballs = q


def spread_fireball(group):
    q = []
    m = s = odd = 0
    x, y = group[0][0], group[0][1]

    for fireball in group:
        m += fireball[2]
        s += fireball[3]
        odd += fireball[4] % 2

    if m // 5 <= 0:  # 소멸
        return []
    if odd == 0 or odd == len(group):  # 모두 짝홀
        for i in range(0, 8, 2):
            heapq.heappush(q, [x, y, m // 5, s // len(group), i])
    else:
        for i in range(1, 8, 2):
            heapq.heappush(q, [x, y, m // 5, s // len(group), i])

    return q


def split_fireball():
    global fireballs
    q = []

    while fireballs:
        group = [heapq.heappop(fireballs)]
        while fireballs:
            next = heapq.heappop(fireballs)
            if (group[0][0], group[0][1]) == (next[0], next[1]):
                group.append(next)
            else:
                heapq.heappush(fireballs, next)
                break

        if len(group) > 1:
            temps = spread_fireball(group)
            for temp in temps:
                heapq.heappush(q, temp)
        else:
            heapq.heappush(q, group[0])

    fireballs = q


def get_m():
    global fireballs

    for _ in range(k):
        # move fireball
        move_fireball()

        # split fireball
        split_fireball()

    result = 0
    for fireball in fireballs:
        result += fireball[2]
    return result


print(get_m())
