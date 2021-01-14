array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
find = 7

def binary_search(array, target, start, end):    
    if start > end: return None
    
    mid = (start + end) // 2
    
    if target == array[mid]: return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

result = binary_search(array, find, 0, len(array) - 1)
if result == None:
    print(result)
else:
    print(result + 1)
