import sys
from collections import deque
input = sys.stdin.readline
num_student, num_compare = map(int, input().split())
graph = [[] for _ in range(num_student)]
indegree = [0 for _ in range(num_student)]

for i in range(num_compare):
    s1, s2 = map(int, input().split())
    graph[s1 - 1].append(s2 - 1)
    indegree[s2 - 1] += 1

queue = deque()
for i in range(num_student):
    if indegree[i] == 0:
        queue.append(i)
result = []
while queue:
    node = queue.popleft()
    result.append(node + 1)

    for vertex in graph[node]:
        indegree[vertex] -= 1
        if indegree[vertex] == 0:
            queue.append(vertex)

print(*result)