import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
num_testcase = int(input())

def solve():
    num_vertex, num_edges = map(int, input().split())
    graph = [[] for i in range(num_vertex)]
    color = [-1] * num_vertex

    for _ in range(num_edges):
        v, e = map(int, input().split())
        graph[v - 1].append(e - 1)
        graph[e - 1].append(v - 1)
    result = False

    for i in range(num_vertex):
        if color[i] == -1:
            result = is_bipartite(graph, color, i, 0)
            if not result:
                break

    msg = "YES" if result else "NO"
    print(msg)

def is_bipartite(graph, color, startsAt, turn) -> bool:
    color[startsAt] = turn
    new_turn = (turn + 1) % 2
    result = True
    for vertex in graph[startsAt]:
        if color[vertex] == -1:
            result = is_bipartite(graph, color, vertex, new_turn)
        elif color[vertex] == turn:
            return False
    return result
        

for i in range(num_testcase):
    solve()