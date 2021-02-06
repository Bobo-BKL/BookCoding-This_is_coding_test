from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
temp = list(map(int, input().split()))

opers = []
for i in range(4):
    for _ in range(temp[i]):
        opers.append(i)

maxs = 0
mins = int(1e9)
for oper in list(permutations(opers, len(opers))):
    num = 0
    op = 0
    result = nums[0]
    
    for i in range(1, 2 * n - 1):
        if i % 2 == 0: 
            num = nums[i // 2]
            if op == 0: result += num
            elif op == 1: result -= num
            elif op == 2: result *= num
            else: 
                if result < 0: result = (abs(result) // num) * -1
                else: result = result // num
        else: op = oper[i // 2]
            
    maxs = max(maxs, result)
    mins = min(mins, result)
    
print(maxs)
print(mins)