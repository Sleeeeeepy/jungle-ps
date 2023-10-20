import sys
from queue import Queue
input = sys.stdin.readline

num_computers = int(input())
num_pairs = int(input())

graph = [[0 for _ in range(num_computers)] for _ in range(num_computers)]
visited = [False] * num_computers
for _ in range(num_pairs):
    computer1, computer2 = map(int, input().split())
    computer1 -= 1
    computer2 -= 1
    graph[computer1][computer2] = 1
    graph[computer2][computer1] = 1

def bfs(startsAt: int) -> int:
    q = Queue()
    q.put(startsAt)
    visited[startsAt] = True
    count = 0    
    while not q.empty():
        computer = q.get()

        for i in range(num_computers):
            if not visited[i] and graph[computer][i] == 1:
                visited[i] = True
                count += 1
                q.put(i)
    return count

print(bfs(0))