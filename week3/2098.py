import sys
input = sys.stdin.readline

num_cities = int(input())
graph = [list(map(int, input().split())) for _ in range(num_cities)]
visited = [[-1 for _ in range(1 << num_cities)] for i in range(num_cities)]
def tsp(start, path):
    global num_cities
    if path == (1 << num_cities) - 1:
        if graph[start][0] == 0:
            return float("inf")
        return graph[start][0]
    
    if visited[start][path] != -1:
        return visited[start][path]
    
    visited[start][path] = float("inf")
    for i in range(num_cities):
        if graph[start][i] == 0:
            continue
        
        if (path & (1 << i)) == (1 << i):
            continue

        visited[start][path] = min(visited[start][path], graph[start][i] + tsp(i, path | (1 << i)))

    return visited[start][path]

print(tsp(0, 1))