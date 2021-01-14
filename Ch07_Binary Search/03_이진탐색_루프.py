array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
find = 7

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target: return mid
        elif array[mid] < target: start = mid + 1
        else: end = mid - 1
        
    return None
    
result = binary_search(array, find, 0, len(array) - 1)
if result == None:
    print(result)
else:
    print(result + 1)