import sys
from queue import Queue

input = sys.stdin.readline

num_vertex, num_edge, startsAt = map(int, input().split())
startsAt -= 1
graph = [[0 for _ in range(num_vertex)] for _ in range(num_vertex)]
visited = [False] * num_vertex
for i in range(num_edge):
    _from, _to = map(int, input().split())
    _from -= 1
    _to -= 1
    graph[_from][_to] = 1
    graph[_to][_from] = 1

def dfs(startsAt):
    global num_vertex
    print(startsAt + 1, end=' ')

    for i in range(num_vertex):
        if not visited[i] and graph[startsAt][i] == 1:
            visited[i] = True
            dfs(i)

visited[startsAt] = True
dfs(startsAt)
print('')
visited = [False] * num_vertex

q = Queue()
q.put(startsAt)
visited[startsAt] = True
while not q.empty():
    node = q.get()
    print(node + 1, end=' ')
    
    for i in range(num_vertex):
        if not visited[i] and graph[node][i] == 1:
            visited[i] = True
            q.put(i)
print('')

