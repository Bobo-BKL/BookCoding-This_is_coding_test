def solution(A, B):
    result = []

    if A >= B:
        b_left = B - (A // 2 + A % 2 - 1)
        while A and B:
            for _ in range(2):
                if A <= 0: break
                result.append('a')
                A -= 1
            if b_left >= 3:
                result.append('b')
                b_left -= 1
                B -= 1
            result.append('b')
            B -= 1
    else:
        a_left = A - (B // 2 + B % 2 - 1)
        while A and B:
            for _ in range(2):
                if B <= 0: break
                result.append('b')
                B -= 1
            if a_left >= 3:
                result.append('a')
                a_left -= 1
                A -= 1
            result.append('a')
            A -= 1
    if A > 0:
        for _ in range(A):
            result.append('a')
    if B > 0:
        for _ in range(B):
            result.append('b')

    return ''.join(result)


print(solution(1, 4))
