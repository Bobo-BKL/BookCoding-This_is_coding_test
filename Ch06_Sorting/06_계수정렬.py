array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

d = [0] * (max(array) + 1)

for i in range(len(array)):
    d[array[i]] += 1
    
print([x for x in range(len(d)) for _ in range(d[x])])
