import heapq

n = int(input())
cards = []

for _ in range(n):
    heapq.heappush(cards, int(input()))

result = 0
while len(cards) != 1:
    smallest = heapq.heappop(cards)
    smallest2 = heapq.heappop(cards)
    sum_val = smallest + smallest2
    heapq.heappush(cards, sum_val)
    result += sum_val

print(result)