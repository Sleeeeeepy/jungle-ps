import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
iceberg = []

for i in range(n):
    iceberg.append(list((map(int, input().split()))))

def find(x, y, visited, melt):
    """
    find all adj from (x, y)
    """
    global n, m
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    melt_count = 0
    while q:
        a, b = q.popleft()
        if iceberg[a][b] == 0:
            continue

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
    
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if iceberg[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
            elif iceberg[nx][ny] == 0:
                melt_count += 1

        if melt_count > 0:
            melt.append((a, b, melt_count))
            melt_count = 0

year = 0
while True:
    count = 0
    is_done = True
    visited = [[False for _ in range(m)] for _ in range(n)]
    melt = deque()
    for i in range(len(iceberg)):
        for j in range(len(iceberg[i])):
            if iceberg[i][j] != 0:
                is_done = False
            
            if not visited[i][j] and iceberg[i][j] != 0:
                find(i, j, visited, melt)
                count += 1

    if count > 1:
        break
    
    if is_done:
        print(0)
        exit()

    while melt:
        x, y, c = melt.popleft()
        iceberg[x][y] = max(0, iceberg[x][y] - c)

    year += 1

print(year)