import sys

input = sys.stdin.readline
stack = []
string = input().strip()
bomb = list(input().strip())
bomb_len = len(bomb)

for c in string:
    stack.append(c)
    if stack[-bomb_len:] == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print("FRULA")