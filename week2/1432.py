import sys
from queue import PriorityQueue

input = sys.stdin.readline
num_vertex = int(input())

outdegree = [0 for i in range(num_vertex)]
graph = [[] for _ in range(num_vertex)]

for i in range(num_vertex):
    _input = list(map(int, input().split('\n')[0]))
    for j in range(len(_input)):
        if _input[j] == 1:
            graph[j].append(i)
            outdegree[i] += 1

queue = PriorityQueue()
for i in range(len(outdegree)):
    if outdegree[i] == 0:
        queue.put(-i)

N = num_vertex
result = [0 for i in range(num_vertex)]
while not queue.empty():
    node = -queue.get()
    result[node] = N

    for i in graph[node]:
        outdegree[i] -= 1
        if outdegree[i] == 0:
            queue.put(-i)
    N -= 1
    
if result.count(0) > 1:
    print(-1)
else:
    print(*result)