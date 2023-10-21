import sys
from queue import Queue
input = sys.stdin.readline

num_cities, num_roads, shortest_path, startsAt = map(int, input().split())
graph = [[] for _ in range(num_cities)]

for i in range(num_roads):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)

distance = [-1] * num_cities
q = Queue()
q.put(startsAt - 1)
distance[startsAt - 1] = 0

while not q.empty():
    node = q.get()

    for city in graph[node]:
        if distance[city] == -1:
            distance[city] = distance[node] + 1
            q.put(city)

result = []
for i in range(num_cities):
    if distance[i] == shortest_path:
        result.append(i + 1)

result.sort()
if len(result) == 0:
    print("-1")
    exit()

for c in result:
    print(c)