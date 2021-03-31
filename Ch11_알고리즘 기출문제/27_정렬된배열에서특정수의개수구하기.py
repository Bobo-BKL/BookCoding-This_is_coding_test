#Counter로 풀 경우
#from collections import Counter

#n, x = map(int, input().split())
#data = list(map(int, input().split()))
#counter = Counter(data)

#print(counter[x])

#Bisect로 풀 경우
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

result = bisect_right(data, x) - bisect_left(data, x)
if result == 0: result = -1

print(result)