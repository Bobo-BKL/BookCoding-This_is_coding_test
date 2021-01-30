import copy

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate_90d_clockwise(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n - i -1] = key[i][j]
            
    return result

def is_unlock(key_length, lock):
    for i in range(key_length):
        for j in range(key_length):
            if lock[key_length + i][key_length + j] != 1: return False
            
    return True
            

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    new_lock = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            new_lock[3 + i][3 + j] = lock[i][j]
            
    for rotate in range(4):
        key = rotate_90d_clockwise(key)
        
        for i in range(n * 2):
            for j in range(n * 2):
                copy_mat = copy.deepcopy(new_lock)
                
                for k in range(n):
                    for l in range(n):
                        copy_mat[i + k][j + l] += key[k][l]
                        
                if is_unlock(m, copy_mat): return True
                
    return False
    
print(solution(key, lock))