from collections import deque

def get_precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    return 0

expr = input()
stack = []
result = []
for token in expr:
    if token.isalpha():
        result.append(token)
    elif token == '(':
        stack.append(token)
    elif token == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and get_precedence(stack[-1]) >= get_precedence(token):
            result.append(stack.pop())
        stack.append(token)
    
while stack:
    result.append(stack.pop())

print(''.join(result))