def solution(n, weak, dist):
    answer = 0
    weak.sort()
    dist.sort(reverse = True)
    
    for person in dist:
        if not weak: break
        
        max_sum = 0
        max_list = []
        max_far = 0
        for now in weak:
            r_list = []
            l_list = []
            r_sum = 0
            l_sum = 0
            # 시계방향
            for i in range(now, now + person + 1):
                i = i % n
                if i in weak:
                    r_sum += 1
                    r_list.append(i)
                    
            # 반시계방향
            for i in range(now - person, now + 1):
                if i < 0: i = n - i
                if i in weak:
                    l_sum += 1
                    l_list.append(i)
            
            if r_sum < l_sum:
                if max_sum < l_sum:
                    max_list = l_list
                    max_sum = l_sum
            elif r_sum > l_sum:
                if max_sum < r_sum:
                    max_list = r_list
                    max_sum = r_sum
            
        answer += 1
        for x in max_list: weak.remove(x)
        print(max_list)
    if weak: answer = -1
    
    return answer
    
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))

weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print(solution(n, weak, dist))
