import sys
input = sys.stdin.readline

def plus_one(x):
    return x + 1

num_vertex = int(input())
graph = dict()

for i in range(num_vertex - 1):
    s, e = map(int, input().split())
    s -= 1
    e -= 1

    if s not in graph:
        temp = []
        temp.append(e)
        graph[s] = temp
    else:
        graph[s].append(e)
    
    if e not in graph:
        temp = []
        temp.append(s)
        graph[e] = temp
    else:
        graph[e].append(s)

stack = []
stack.append(0)
parent = [-1 for _ in range(num_vertex)]
parent[0] = -2
while stack:
    node = stack.pop()
    
    for i in graph[node]:
        if parent[i] == -1:
            parent[i] = node
            stack.append(i)

for i in parent:
    if i < 0:
        continue
    print(i + 1)