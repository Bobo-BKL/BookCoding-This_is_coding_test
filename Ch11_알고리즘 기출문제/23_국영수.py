#n = int(input())

#data = []
#for _ in range(n):
#    data.append(input().split())

n = 12
data = [['Junkyu', '50', '60', '100'],
        ['Sangkeun', '80', '60', '50'],
        ['Sunyoung', '80', '70', '100'],
        ['Soong', '50', '60', '90'],
        ['Haebin', '50', '60', '100'],
        ['Kangsoo', '60', '80', '100'],
        ['Donghyuk', '80', '60', '100'],
        ['Sei', '70', '70', '70'],
        ['Wonseob', '70', '70', '90'],
        ['Sanghyun', '70', '70', '80'],
        ['nsj', '80', '80', '80'],
        ['Taewhan', '50', '60', '90']
    ]
data.sort(key = lambda data : (-int(data[1]), int(data[2]), -int(data[3]), (data[0])))

for i in data:
    print(i[0])