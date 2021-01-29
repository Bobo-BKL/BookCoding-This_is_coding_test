def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2+ 1):
        prev = s[0:step]
        rept = 1
        sum = ''
        for i in range(step, len(s), step):
            if prev == s[i:i + step]:
                rept += 1
            else:
                if rept >= 2:
                    sum += str(rept) + prev
                else: sum += prev
                
                rept = 1
                prev = s[i:i + step]
                
        sum += str(rept) + prev if rept >= 2 else prev
        answer = min(answer, len(sum))
    
    return answer
    
print(solution('aabbaccc'))