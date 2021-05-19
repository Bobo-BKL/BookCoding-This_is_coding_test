def solution(A):
    left = A[0]
    right = sum(A[1:])
    result = abs(left - right)

    for elem in A[1:-1]:
        left += elem
        right -= elem
        result = min(result, abs(left - right))
        if result == 0: break

    return result


print(solution([100, 3, 1, 2, 4, 3, 5, 9, 7, 1, 2, 10, 100]))
