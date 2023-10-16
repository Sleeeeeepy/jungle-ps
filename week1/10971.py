import sys
input = sys.stdin.readline

num_cities = int(input())
graph = []

for i in range(num_cities):
    costs = list(map(int, input().split()))
    graph.append(costs)

min_cost = 2147483647
visited = [False for _ in range(num_cities)]
def tsp(start, current_cost):
    global min_cost
    global num_cities

    if False not in visited:
        if graph[start][0] == 0:
            return
        min_cost = min(min_cost, current_cost + graph[start][0])

    for i in range(num_cities):
        if graph[start][i] != 0 and not visited[i]:
            visited[i] = True
            tsp(i, current_cost + graph[start][i])
            visited[i] = False

visited[0] = True
tsp(0, 0)
print(min_cost)
