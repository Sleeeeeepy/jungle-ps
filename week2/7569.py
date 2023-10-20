import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 0, 1, 0, 0, -1]
dy = [0, 1, 0, 0, -1, 0]
dz = [1, 0, 0, -1, 0, 0]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k))

while q:
    z, x, y = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
            continue

        if box[nz][nx][ny] == 0:
            box[nz][nx][ny] = box[z][x][y] + 1
            q.append((nz, nx, ny))

_max = -1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print("-1")
                exit()
            else:
                _max = max(_max, box[i][j][k])

print(_max - 1)