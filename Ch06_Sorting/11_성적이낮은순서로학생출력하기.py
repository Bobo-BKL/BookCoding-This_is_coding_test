n = int(input())

array = []
for _ in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))
    
array = sorted(array, key = lambda student: student[1])

for i in array:
    print(i[0], end = ' ')