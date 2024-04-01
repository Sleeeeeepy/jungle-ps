N = int(input())
reverse_polish = input()
id = dict()
for i in range(N):
    id[chr(65 + i)] = int(input())

def isOperator(ch):
    if ch == '*':
        return True

    if ch == '+':
        return True
    
    if ch == '/':
        return True
    
    if ch == '-':
        return True
    
    return False

def evaluate(left, right, op):
    if op == '*':
        return left * right

    if op == '+':
        return left + right
    
    if op == '/':
        return left / right
    
    if op == '-':
        return left - right
    
    raise SyntaxError(f'Unkown operator {op}.')

num_stack = []
for s in reverse_polish:
    if isOperator(s):
        if len(num_stack) < 2:
            raise SyntaxError('Invalid syntax.')
        right = num_stack.pop()
        left = num_stack.pop()
        num_stack.append(evaluate(left, right, s))
        continue

    num_stack.append(id[s])

print(f'{num_stack.pop():.2f}')