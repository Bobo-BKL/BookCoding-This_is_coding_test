n = int(input())

user = list(map(int, input().split()))

cnt_user = len(user)
answer = []
for stage in range(1, n + 1):
    failed = user.count(stage)

    if cnt_user == 0:
        fail = 0
    else:
        fail = failed / cnt_user

    answer.append((fail, stage))
    cnt_user -= failed

answer.sort(key = lambda x : (-x[0], x[1]))

answer = [i[1] for i in answer]
print(answer)