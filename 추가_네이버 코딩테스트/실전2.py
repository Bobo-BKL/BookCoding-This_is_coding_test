
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


def permutation(data, r):
    result = ''

    def permute(p, indexs):
        nonlocal result

        if result != '': return

        if len(p) == r:
            if not check_3(p, 'a'): return
            if not check_3(p, 'b'): return
            result = ''.join(p)
            return

        for i, element in enumerate(data):
            if i in indexs: continue
            permute(p + [element], indexs + [i])

    permute([], [])
    return result


def solution(A, B):
    data = []
    for _ in range(A):
        data.append('a')
    for _ in range(B):
        data.append('b')

    return permutation(data, A + B)


print(solution(5, 5))
