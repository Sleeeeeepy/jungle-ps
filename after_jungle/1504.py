import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(E):
    s, e, c = map(int, input().split())
    s -= 1
    e -= 1
    graph[s].append((e, c))
    graph[e].append((s, c))

layover1, layover2 = map(int, input().split())
layover1 -= 1
layover2 -= 1
def shortest_path(graph, startsAt, endsAt):
    distance = [2147483647] * N
    q = []
    heapq.heappush(q, (0, startsAt))
    distance[startsAt] = 0
    while q:
        cost, vertex = heapq.heappop(q)
        if distance[vertex] < cost:
            continue
        
        for vert, dist in graph[vertex]:
            if distance[vert] > distance[vertex] + dist:
                distance[vert] = distance[vertex] + dist
                heapq.heappush(q, (distance[vert], vert))
    
    return distance[endsAt]

result1 = shortest_path(graph, 0, layover1) + shortest_path(graph, layover1, layover2) + shortest_path(graph, layover2, N - 1)
result2 = shortest_path(graph, 0, layover2) + shortest_path(graph, layover2, layover1) + shortest_path(graph, layover1, N - 1)
print(-1 if result1 >= 2147483647 and result2 >= 2147483647 else min(result1, result2))