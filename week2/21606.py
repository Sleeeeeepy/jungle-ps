import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
num_nodes = int(input())

def to_inside(n: str) -> bool:
    return n == '1'

is_inside = [False] + list(map(to_inside, list(input().split('\n')[0])))
visited = [False for _ in range(num_nodes + 1)]
path = dict()
answer = 0
for _ in range(num_nodes - 1):
    start, end = map(int, input().split())
    
    if start in path:
        path[start].append(end)
    else:
        path[start] = [end]

    if end in path:
        path[end].append(start)
    else:
        path[end] = [start]

    if is_inside[start] and is_inside[end]:
        answer += 2

def find(startsAt):
    result = 0
    for i in path[startsAt]:
        if not is_inside[i] and not visited[i]:
                visited[i] = True
                result += find(i)
        elif not visited[i]:
            result += 1
    
    return result

for i in range(1, num_nodes + 1):
    j = 0
    if not is_inside[i] and not visited[i]:
        visited[i] = True
        j = find(i)
    
    answer += j * (j - 1)

print(answer)