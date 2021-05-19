from collections import Counter


def solution(A):
    counter = Counter(A)

    result = 0
    for key, val in counter.items():
        if val % 2:
            result = key
            break

    return result


print(solution([9, 3, 9, 3, 9, 7, 9]))
