stack = []
brackets = input()

def error():
    print("0")
    exit()

for b in brackets:
    if b == "(":
        stack.append("(")
    elif b == "[":
        stack.append("[")
    elif b == ")":
        if not stack or stack[-1] == "[":
            error()
        if stack[-1].isnumeric():
            num = int(stack.pop())
            while stack and stack[-1].isnumeric():
                if stack and stack[-1].isnumeric():
                    num += int(stack.pop())
            if (stack and stack[-1] == "("):
                stack.pop()
            else:
                error()
            stack.append(f"{num * 2}")
        elif stack[-1] == "(":
            stack.pop()
            stack.append("2")
    elif b == "]":
        if not stack or stack[-1] == "(":
            error()
        if stack[-1].isnumeric():
            num = int(stack.pop())
            while stack and stack[-1].isnumeric():
                if stack and stack[-1].isnumeric():
                    num += int(stack.pop())
            if (stack and stack[-1] == "["):
                stack.pop()
            else:
                error()
            stack.append(f"{num * 3}")
        elif stack[-1] == "[":
            stack.pop()
            stack.append("3")

result = 0
for s in stack:
    if s.isnumeric():
        result += int(s)
    else:
        error()
print(result)