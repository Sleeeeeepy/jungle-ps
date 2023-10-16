import sys
input = sys.stdin.readline

input()
tower = list(map(int, input().split()))
stack = []
answer = [0 for _ in range(len(tower))]

for i in range(len(tower)):
    if stack and tower[stack[-1]] < tower[i]:
        while stack:
            if tower[stack[-1]] < tower[i]:
                stack.pop()
            else:
                answer[i] = stack[-1] + 1
                break
        stack.append(i)
    elif stack and tower[stack[-1]] >= tower[i]:
        answer[i] = stack[-1] + 1
        stack.append(i)
    else:
        stack.append(i)

print(*answer)