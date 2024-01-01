import sys

input = sys.stdin.readline
input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = set()
for i in A:
    s.add(i)

for i in B:
    if i in s:
        s.remove(i)
    else:
        s.add(i)

print(len(s))