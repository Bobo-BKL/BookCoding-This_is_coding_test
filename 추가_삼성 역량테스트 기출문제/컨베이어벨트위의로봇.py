n, k = map(int, input().split())
belt_life = list(map(int, input().split()))
robots_on_belt = [False] * n


def turn_beltlife():
    global belt_life, robots_on_belt

    temp = belt_life[2 * n - 1]
    for i in range(1, 2 * n):
        belt_life[-i] = belt_life[-i - 1]
    belt_life[0] = temp

    for i in range(1, n):
        robots_on_belt[-i] = robots_on_belt[-i - 1]
    robots_on_belt[0] = False
    robots_on_belt[n - 1] = False


def turn_robots():
    global robots_on_belt, belt_life
    to_zero = 0

    for i in range(1, n):
        if robots_on_belt[-i - 1]:
            if (not robots_on_belt[-i]) and belt_life[-(i + n)] > 0:
                robots_on_belt[-i] = True
                robots_on_belt[-i - 1] = False
                belt_life[-(i + n)] -= 1
                if belt_life[-(i + n)] == 0: to_zero += 1

    if (not robots_on_belt[0]) and belt_life[0] > 0:
        robots_on_belt[0] = True
        belt_life[0] -= 1
        if belt_life[0] == 0: to_zero += 1

    robots_on_belt[n - 1] = False

    return to_zero


def get_step():
    global belt_life
    empty = 0
    step = 0

    while True:
        if empty >= k: break
        step += 1

        # 1 - 벨트 한칸 회전
        turn_beltlife()

        # 2 - 먼저 올라간 로봇 회전 방향으로 한칸 이동
        empty += turn_robots()

    return step


print(get_step())