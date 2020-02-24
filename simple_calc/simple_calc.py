OPS = {
	'+': lambda a, b: a + b,
	'-': lambda a, b: a - b,
	'*': lambda a, b: a * b,
	'/': lambda a, b: a / b
}


def calc(expression):
	expression = expression.replace(' ', '')
	expression = handle_unar(expression)
	stack = []
	to_rpn(expression, stack)
	return calc_stack(stack)


def calc_stack(st):
	global OPS
	j = 0
	while len(st) > 1:
		j += 1
		for i, x in enumerate(st):
			if x in (OPS.keys()):
				st = st[:i - 2] + [OPS[x](st[i - 2], st[i - 1])] + st[i + 1:]
				break
		if j == 1000:
			break
	return st[0]


def to_rpn(expression, stack):
	tmp_stack = []
	nbr = ''
	for ch in expression:
		if ch.isdigit():
			nbr += ch
			continue
		elif nbr:
			stack.append(int(nbr))
			nbr = ''
		if ch == '(':
			tmp_stack.append(ch)
		elif ch == ')':
			while tmp_stack[-1] != '(':
				stack.append(tmp_stack.pop())
			tmp_stack.pop()
		else:
			if ch in ('+-'):
				while tmp_stack and tmp_stack[-1] in ('*/'):
					stack.append(tmp_stack.pop())
			if ch == '-':
				while tmp_stack and tmp_stack[-1] in ('+-'):
					stack.append(tmp_stack.pop())
			tmp_stack.append(ch)
	if nbr:
		stack.append(int(nbr))
	while tmp_stack:
		stack.append(tmp_stack.pop())


def handle_unar(expr):
	""" replace all unar minus to (0-x)"""
	i = 0
	while i < len(expr):
		if expr[i] == '-' and (not i or expr[i - 1] in ('-+*/(')):
			expr = expr[:i] + '(0' + expr[i:]
			expr = insert_close_bracet(expr, i + 3)
		i += 1
	return expr


def insert_close_bracet(expression, i):
	if i == len(expression):
		return expression + ')'
	elif expression[i].isdigit():
		while i != len(expression) and expression[i].isdigit():
			i += 1
		return expression[:i] + ')' + expression[i:]
	else:
		brackets = 1
		while brackets:
			i += 1
			if i == len(expression) or expression[i] == ')':
				brackets -= 1
			elif expression[i] == '(':
				brackets += 1
		return expression[:i] + ')' + expression[i:]


# print(calc('-7 * -(6 / 3 + 2)'))
# print(calc(input()))
