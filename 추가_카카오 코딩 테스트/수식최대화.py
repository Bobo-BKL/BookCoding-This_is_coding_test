import re
from itertools import permutations


def solution(expression):
	opers = [x for x in ['*', '+', '-'] if x in expression]
	opers = [list(y) for y in permutations(opers)]
	ex = re.split('(\D)', expression)  # 소괄호하면 기타 잘려나간 것들도 저장됨, d: 하나하나 D: 자릿수까지 포함

	result = 0
	for oper in opers:
		_ex = ex[:]  # 얕은복사, 1차원 리스트의 경우 문제 없음
		for op in oper:
			while op in _ex:
				tmp = _ex.index(op)
				_ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
				_ex = _ex[:tmp]+_ex[tmp+2:]
		result = max(result, abs(int(_ex[0])))

	return result


print(solution("100-200*300-500+20"))
