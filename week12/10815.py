import sys

input = sys.stdin.readline
input()
N = list(map(int, input().split()))
input()
M = list(map(int, input().split()))

s = set()
for i in N:
    s.add(i)

result = []
for i in M:
    if i in s:
        result.append(1)
        continue
    result.append(0)

print(*result, sep=' ')