import sys
from queue import PriorityQueue
input = sys.stdin.readline

num_cities = int(input())
num_buses = int(input())
graph = [[float("inf") for _  in range(num_cities)] for _ in range(num_cities)]
distance = [float("inf") for _ in range(num_cities)]

INF = float("inf")
for i in range(num_buses):
    start, end, value = map(int, input().split())
    start -= 1
    end -= 1
    graph[start][end] = min(graph[start][end], value)

startsAt, endsAt = map(lambda x: x - 1, map(int, input().split()))

# find shortest path
pq = PriorityQueue()
distance[startsAt] = 0
pq.put((0, startsAt))
while not pq.empty():
    dist, node = pq.get()
    if distance[node] < dist:
        continue

    for i in range(num_cities):
        if graph[node][i] == INF:
            continue
        
        if distance[i] > dist + graph[node][i]:
            distance[i] = dist + graph[node][i]
            pq.put((distance[i], i))

print(distance[endsAt])