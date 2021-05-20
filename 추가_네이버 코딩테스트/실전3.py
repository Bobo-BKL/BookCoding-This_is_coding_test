from collections import Counter


def count_uni(str):
    counter = Counter(list(str))
    result = 0
    for cnt in counter.values():
        if cnt == 1:
            result += 1
    return result


def solution(S):
    result = 0

    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            result += count_uni(S[i:j])

    return result % 1000000007

print(len('DJFKRUEBEMVCLVJURBEKSLXIVCHGBRMDLCLDGEVDJDUEGBMSIIWNDBHVGRVENSJCBCJVYFVDCEBSMXGVKDJRHFKDLWHFIGNRNFFJ'))
print(solution('DJFKRUEBEMVCLVJURBEKSLXIVCHGBRMDLCLDGEVDJDUEGBMSIIWNDBHVGRVENSJCBCJVYFVDCEBSMXGVKDJRHFKDLWHFIGNRNFFJ'))