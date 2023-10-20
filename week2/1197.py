import sys
input = sys.stdin.readline
num_vertices, num_edges = map(int, input().split())
edges = []
parent = [0 for _ in range(num_vertices + 1)] 

for i in range(num_edges):
    startsAt, endsAt, value = map(int, input().split())
    edges.append((startsAt, endsAt, value))

for i in range(len(parent)):
    parent[i] = i
    
edges.sort(key=lambda x: x[2])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[b] = parent[a]
        return
    parent[a] = parent[b]

result = 0
for edge in edges:
    start, end, value = edge
    if find(start) != find(end):
        union(start, end)
        result += value

print(result)