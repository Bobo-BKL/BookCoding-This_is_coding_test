key = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]]
lock = [[1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1]]

def rotate_90d_clockwise(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
            
    return result

def is_unlock(lock_length, key_len, lock):
    for i in range(lock_length):
        for j in range(lock_length):
            if lock[(key_len - 1) + i][(key_len -1) + j] != 1: 
                return False
            
    return True

def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)
    
    new_lock_len = lock_len + (key_len - 1) * 2
    new_lock = [[0] * new_lock_len for _ in range(new_lock_len)]
    for i in range(lock_len):
        for j in range(lock_len):
            new_lock[(key_len - 1) + i][(key_len - 1) + j] = lock[i][j]
            
    for rotate in range(4):
        key = rotate_90d_clockwise(key)
        
        for i in range(new_lock_len - (key_len - 1)):
            for j in range(new_lock_len - (key_len - 1)):
                
                for k in range(key_len):
                    for l in range(key_len):
                        new_lock[i + k][j + l] += key[k][l]
                        
                if is_unlock(lock_len, key_len, new_lock): return True
                
                for k in range(key_len):
                    for l in range(key_len):
                        new_lock[i + k][j + l] -= key[k][l]
                
    return False
    
print(solution(key, lock))
