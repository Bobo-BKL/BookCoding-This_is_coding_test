n = int(input())
nums = list(map(int, input().split()))
oper_num = list(map(int, input().split()))

Max = -int(1e9)
Min = int(1e9)

def operate(a, b, oper, cnt):
    global oper_num, Max, Min

    if oper == 0:
        dfs(cnt, a + b)
    elif oper == 1:
        dfs(cnt, a - b)
    elif oper == 2:
        dfs(cnt, a * b)
    else:
        dfs(cnt, int(a / b))

def dfs(cnt, result):
    global oper_num, Max, Min

    if cnt == n:
        Max = max(Max, result)
        Min = min(Min, result)
    else:
        for i in range(4):
            if oper_num[i] > 0:
                oper_num[i] -= 1
                operate(result, nums[cnt], i, cnt + 1)
                oper_num[i] += 1
    
dfs(1, nums[0])
print(Max)
print(Min)