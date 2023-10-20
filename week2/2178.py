import sys
from queue import Queue
input = sys.stdin.readline

height, width = map(int, input().split())
goal_h, goal_w = height - 1, width - 1

_map = []
for i in range(height):
    row = list(input().split('\n')[0])
    row = list(map(int, row))
    _map.append(row)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = Queue()
q.put((0, 0))
_map[0][0] = 1

while not q.empty():
    x, y = q.get()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # 인덱스 범위 초과
        if nx >= height or nx < 0 or ny >= width or ny < 0:
            continue
        
        # 벽
        if _map[nx][ny] == 0:
            continue
        
        # 이미 방문
        if _map[nx][ny] != 1:
            continue

        _map[nx][ny] = _map[x][y] + 1

        q.put((nx, ny))

print(_map[goal_h][goal_w])