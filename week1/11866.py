from collections import deque

dead = []
q = deque()
n, k = map(int, input().split())

for i in range(1, n + 1):
    q.append(i)

while True:
    if (len(q) == 0):
        break

    for i in range(k):
        q.append(q.popleft())
    dead.append(q.pop())

print("<", end="")
for i in range(len(dead) - 1):
    print(f"{dead[i]}, ", end="")
print(f"{dead[-1]}>", end="")