def permutation(data, r):
    result = []

    def permute(p, index):
        if len(p) == r:
            result.append(p)
            return
        for i, element in enumerate(data):
            if index == i: continue
            permute(p + [element], i)

    permute([], -1)
    return result


print(permutation([1, 1, 2], 2))