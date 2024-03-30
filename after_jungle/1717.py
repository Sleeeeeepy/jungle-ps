import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, num_op = map(int, input().split())
_set = [i for i in range(n + 1)]

def find(x):
    if _set[x] == x:
        return x
    _set[x] = find(_set[x])
    return _set[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if x > y:
        _set[x] = y    
    else:
        _set[y] = x

for i in range(num_op):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    elif op == 1:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")