data = []
for _ in range(4):
    data.append(list(map(int, input())))
k = int(input())
instruction = []
for _ in range(k):
    num, way = map(int, input().split())
    instruction.append((num - 1, way))

def cycle(num, way):
    global data
    if way == -1:
        temp = data[num][0]
        for i in range(1, 8):
            data[num][i - 1] = data[num][i]
        data[num][7] = temp
    else:
        temp = data[num][7]
        for i in range(7, 0, -1):
            data[num][i] = data[num][i - 1]
        data[num][0] = temp

def process(num, way):
    is_cycle = [0] * 4
    is_cycle[num] = way
    # is cycle num left side
    for i in range(num, 0, -1):
        if data[i - 1][2] == data[i][6]: break
        is_cycle[i - 1] = -is_cycle[i]
    # is cycle num right side
    for i in range(num, 3):
        if data[i][2] == data[i + 1][6]: break
        is_cycle[i + 1] = -is_cycle[i]
    # do cycle
    for i in range(4):
        if is_cycle[i] != 0:
            cycle(i, is_cycle[i])

for num, way in instruction:
    process(num, way)

result = 0
for i in range(4):
    if data[i][0] != 0:
        result += pow(2, i)
print(result)