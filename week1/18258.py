import sys
from collections import deque
input = sys.stdin.readline

num_cmd = int(input())
q = deque()

for _ in range(num_cmd):
    cmd = input().split()

    if cmd[0] == "push":
        arg = int(cmd[1])
        q.append(arg)
    elif cmd[0] == "pop":
        if not q:
            print(-1)
            continue
        print(q.popleft())
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        print(1 if len(q) == 0 else 0)
    elif cmd[0] == "front":
        if not q:
            print(-1)
            continue
        print(q[0])
    elif cmd[0] == "back":
        if not q:
            print(-1)
            continue
        print(q[-1])