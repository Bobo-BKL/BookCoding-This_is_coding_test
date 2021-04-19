import heapq
r, c, k = map(int, input().split())

data = [[0] * 100 for _ in range(100)]
for i in range(3):
    data[i][0], data[i][1], data[i][2] = map(int, input().split())

row_len = 3
col_len = 3


def line_repair(array):
    temp = []

    nums = [0] * (100 + 1)
    q = []
    for num in array:
        nums[num] += 1

    for num in range(1, 100 + 1):
        if nums[num] == 0: continue
        heapq.heappush(q, (nums[num], num))

    count = 0
    while q and count < 100:
        a, b = heapq.heappop(q)
        temp.append(b)
        temp.append(a)
        count += 2

    length = len(temp)
    while len(temp) < 100:
        temp.append(0)

    return length, temp

def r_cal():
    global data
    max_len = 0

    for row in range(100):
        if sum(data[row]) == 0: break
        length, data[row] = line_repair(data[row])
        max_len = max(length, max_len)

    return max_len

def c_cal():
    global data
    max_len = 0

    for col in range(100):
        list_col = [data[row][col] for row in range(100)]
        if sum(list_col) == 0: break
        length, temp = line_repair(list_col)

        for row in range(100):
            data[row][col] = temp[row]
        max_len = max(length, max_len)

    return max_len


result = 0
while result <= 100:
    if data[r - 1][c - 1] == k: break

    if row_len >= col_len: col_len = r_cal()
    else: row_len = c_cal()

    result += 1


if result <= 100: print(result)
else: print(-1)