import sys
from collections import deque
input = sys.stdin.readline

num_cities = int(input())
num_roads = int(input())
graph = {}
transpose = {}
indegree = [0] * (num_cities + 1)
result = [0] * (num_cities + 1)
visited = [False] * (num_cities + 1)
for i in range(1, num_cities + 1):
    graph[i] = []
    transpose[i] = []

for i in range(num_roads):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))
    transpose[e].append((s, v))
    indegree[e] += 1

startsAt, endsAt = map(int, input().split())

queue = deque()
queue.append(startsAt)

# topological sort
while queue:
    node = queue.popleft()

    for vertex, value in graph[node]:
        indegree[vertex] -= 1
        result[vertex] = max(result[vertex], result[node] + value)
        if indegree[vertex] == 0:
            queue.append(vertex)

# bfs starts at 'endsAt'
queue.clear()
queue.append(endsAt)
visited[endsAt] = True
count = 0
while queue:
    node = queue.popleft()
    for vertex, value in transpose[node]:
        if result[node] != result[vertex] + value:
            continue
        count += 1
        if not visited[vertex]:
            visited[vertex] = True
            queue.append(vertex)
print(result[endsAt])
print(count)
