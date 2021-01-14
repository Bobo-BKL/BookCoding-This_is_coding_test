import sys

n = int(input())
store = list(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

store.sort()

def binary_search(store, f_item, start, end):
    if start > end: return 'no'
    
    mid = (start + end) // 2
    
    if store[mid] == f_item: return 'yes'
    elif store[mid] > f_item: return binary_search(store,f_item,  start, mid - 1)
    else: return binary_search(store, f_item, mid + 1, end)
    
for i in range(m):
    print(binary_search(store, find[i], 0, n - 1), end = ' ')