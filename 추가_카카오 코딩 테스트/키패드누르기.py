pad = [
    (1, 4, 7),
    (2, 5, 8, 0),
    (3, 6, 9)
]


def solution(numbers, hand):
    answer = ''

    left_idx = [0, 3]
    right_idx = [2, 3]

    for num in numbers:
        if num in pad[0]:
            answer += 'L'
            left_idx = [0, pad[0].index(num)]

        elif num in pad[2]:
            answer += 'R'
            right_idx = [2, pad[2].index(num)]

        else:
            num_idx = [1, pad[1].index(num)]
            temp = (abs(left_idx[0] - num_idx[0]) + abs(left_idx[1] - num_idx[1])) - (
                        abs(right_idx[0] - num_idx[0]) + abs(right_idx[1] - num_idx[1]))
            if temp > 0:
                right_idx = num_idx
                answer += 'R'
            elif temp < 0:
                left_idx = num_idx
                answer += 'L'
            else:
                if hand == 'left':
                    left_idx = num_idx
                    answer += 'L'
                else:
                    right_idx = num_idx
                    answer += 'R'

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
