import sys
from queue import Queue
input = sys.stdin.readline

num_vertices, num_edges = map(int, input().split())
graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
visited = [False for _ in range(num_vertices)]

for i in range(num_edges):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    graph[start][end] = 1
    graph[end][start] = 1

def bfs(startsAt: int) -> bool:
    q = Queue()
    q.put(startsAt)

    found = False
    while not q.empty():
        node = q.get()

        for i in range(num_vertices):
            if not visited[i] and graph[node][i] == 1:
                visited[i] = True
                q.put(i)
                found = True
    return found

count = 0
for i in range(num_vertices):
    if bfs(i):
        count += 1

for i in range(num_vertices):
    if visited[i] == False:
        count += 1
print(count)