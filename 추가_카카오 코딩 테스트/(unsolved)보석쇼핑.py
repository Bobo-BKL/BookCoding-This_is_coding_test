def solution(gems):
    answer = []
    gemstone = len(set(gems))

    min_len = int(1e9)
    for idx, inst in enumerate(gems):
        collected = [inst]
        count = gemstone - 1
        col_cnt = 0
        for inst2 in gems[idx + 1:]:
            if count <= 0: break
            if inst2 not in collected:
                collected.append(inst2)
                count -= 1
            col_cnt += 1

        if count <= 0 and (min_len > col_cnt):
            answer = [idx + 1, idx + 1 + col_cnt]
            min_len = col_cnt

        if min_len == 0: break

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))