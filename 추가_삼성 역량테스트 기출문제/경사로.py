import copy

n, l = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

result = 0

def is_same_floor(line):
    for i in range(n):
        if line[0] != line[i]: return False
    return True

def is_level_1diff(line):
    for i in range(1, n):
        if abs(line[i - 1] - line[i]) > 1: return False
    return True

def is_cliff(line):
    checked = [False] * (n)
    for b in range(1, n):
        # after is bigger
        if line[b - 1] < line[b]:
            for a in range(b - 1, b - l - 1, -1):
                if 0 <= a and line[b - 1] == line[a] and not checked[a]:
                    checked[a] = True
                else: return False
            checked[b - 1] = True
        # before is bigger
        elif line[b - 1] > line[b]:
            for a in range(b, b + l):
                if a < n and line[b] == line[a] and not checked[a]:
                    checked[a] = True
                else: return False
            checked[b] = True
    return True

def is_available(line):
    if is_same_floor(line): return True
    if not is_level_1diff(line): return False
    if is_cliff(line): return True
    return False

for i in range(n):
    row = copy.deepcopy(data[i])
    col = copy.deepcopy([data[j][i] for j in range(n)])
    
    if is_available(row): result += 1
    if is_available(col): result += 1
print(result)
