def permutation(data, r):
    result = []

    def permute(p, indexs):
        if len(p) == r:
            result.append(p)
            return
        for i, element in enumerate(data):
            if i in indexs: continue
            permute(p + [element], indexs + [i])

    permute([], [])
    return result


print(permutation((1, 2, 3, 4), 3))
