def combination(data, r):
    result = []

    def combine(c, index):
        if len(c) == r:
            result.append(c)
            return
        for i, element in enumerate(data):
            if i <= index: continue
            combine(c + [element], i)

    combine([], -1)
    return result


print(combination([1, 2, 3, 4], 4))