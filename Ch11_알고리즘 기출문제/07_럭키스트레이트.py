n = list(map(int, input()))

m = len(n)

left = 0
right = 0
for i in range(m // 2):
    left += n[i]
    right += n[m - 1 - i]
    
if left == right: print('LUCKY')
else: print("READY")