import copy
from collections import deque

n, m, gas = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
taxi_x, taxi_y = map(lambda x: int(x) - 1, input().split())
customers = []
for _ in range(m):
    li = list(map(lambda x: int(x) - 1, input().split()))
    customers.append([True, li[0], li[1], li[2], li[3]])

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def find_close_customer():
    data = copy.deepcopy(graph)

    # bfs
    q = deque([(taxi_x, taxi_y, 2)])
    data[taxi_x][taxi_y] = 2
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
                data[nx][ny] = dist + 1
                q.append((nx, ny, dist + 1))

    # 각 자리중 가장 작은 값 구출
    number = min_dist = int(1e9)
    for cus_num in range(m):
        if not customers[cus_num][0]: continue
        _, x, y, _, _ = customers[cus_num]
        if data[x][y] <= 1: continue
        if min_dist > data[x][y]:
            min_dist = data[x][y]
            number = cus_num
        elif min_dist == data[x][y]:  # 값이 같으면 행비교
            if customers[number][1] < x: continue
            elif customers[number][1] == x:  # 행도 같으면 열비교
                if customers[number][2] < y: continue
            min_dist = data[x][y]
            number = cus_num

    # 손님이 더 이상 없거나, 손님께 닿을수 없을 때
    if min_dist >= int(1e9): return -1, -1
    return number, min_dist - 2


def get_customer_to_home(cus_num):
    data = copy.deepcopy(graph)
    _, x, y, fx, fy = customers[cus_num]

    # bfs
    q = deque([(x, y, 2)])
    data[x][y] = 2
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
                if (nx, ny) == (fx, fy): return (dist + 1) - 2
                data[nx][ny] = dist + 1
                q.append((nx, ny, dist + 1))

    return -1


def get_final_gas():
    global taxi_x, taxi_y, gas, customers

    while True:
        # 가까운 승객 구하기
        customer_num, dist_taxi2custom = find_close_customer()
        if customer_num == -1: break
        
        # 승객을 목적지까지 이동
        dist_custom2home = get_customer_to_home(customer_num)
        if dist_custom2home == -1: break

        # 남은 가스 계산 및 해당승객 완료처리
        gas -= dist_taxi2custom
        if gas < 0: break

        gas -= dist_custom2home
        if gas < 0: break

        gas += dist_custom2home * 2

        customers[customer_num][0] = False
        taxi_x, taxi_y = customers[customer_num][3], customers[customer_num][4]

        # 가스 다 끝나면 그만~
        if gas == 0: break

    # 상황파악
    for custom in customers:
        if custom[0]: return -1
    return gas


print(get_final_gas())
