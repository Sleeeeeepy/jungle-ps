import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = set()
result = []
for i in range(n):
    N.add(input().rstrip())

for i in range(m):
    user_input = input().rstrip()
    if user_input in N:
        result.append(user_input)

result.sort()
print(len(result))
for s in result:
    print(s)