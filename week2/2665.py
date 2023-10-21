import sys
from collections import deque

input = sys.stdin.readline
MAX = float("inf")
n = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maze = []
for i in range(n):
    maze.append(list(map(int, list(input().split('\n')[0]))))

# inf: not visited
# 0: visited
visited = [[MAX for _ in range(n)] for _ in range(n)]
start = (0, 0)
visited[0][0] = 0
end = (n - 1, n - 1)
q = deque()
q.append(start)
while q:
    x, y = q.popleft()
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            continue
        
        if visited[nx][ny] > visited[x][y] and maze[nx][ny] == 1:
            visited[nx][ny] = visited[x][y]
            q.append((nx, ny))
            continue

        if visited[nx][ny] > visited[x][y] + 1 and maze[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

result = visited[n - 1][n - 1] if visited[n - 1][n - 1] != MAX else 0
print(result)