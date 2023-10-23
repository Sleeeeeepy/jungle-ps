import sys
from collections import deque
input = sys.stdin.readline

num_parts = int(input())
num_relationships = int(input())
indegree = [0 for _ in range(num_parts + 1)]
parts_table = [0 for _ in range(num_parts + 1)]
is_primitive = [True for _ in range(num_parts + 1)]
parts_table[num_parts] = 1
is_primitive[num_parts] = False
graph = dict()

for i in range(num_relationships):
    x, y, k = map(int, input().split())
    if x not in graph:
        graph[x] = []
    
    if y not in graph:
        graph[y] = []

    graph[x].append((y, k))
    indegree[y] += 1
    is_primitive[x] = False

# topological sort
q = deque()
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    node = q.popleft()
    result.append(node)
    for next, needs in graph[node]:
        parts_table[next] += parts_table[node] * needs
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

for i in range(1, num_parts):
    if is_primitive[i]:
        print(f"{i} {parts_table[i]}")