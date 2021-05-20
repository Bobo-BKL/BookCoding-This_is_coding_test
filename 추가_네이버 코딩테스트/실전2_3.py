from itertools import permutations


def check_3(array, ch):
    a_start = False
    a_cnt = 0
    for inst in array:
        if inst == ch:
            a_cnt += 1
            a_start = True
        else:
            if a_start:
                if a_cnt >= 3:
                    return False
            a_cnt = 0
            a_start = False

    if a_start:
        if a_cnt >= 3:
            return False

    return True


def solution(A, B):
    data = []
    for _ in range(A):
        data.append('a')
    for _ in range(B):
        data.append('b')

    for perm in list(permutations(data, A + B)):
        # A연속 3이상인가?
        if not check_3(perm, 'a'): continue
        if not check_3(perm, 'b'): continue
        return ''.join(perm)


print(solution(8, 3))
