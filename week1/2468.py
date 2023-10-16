import sys
from queue import Queue

input = sys.stdin.readline

map_size = int(input())
_map = []
max_height = -1
visited = [[False for _ in range(map_size)] for _ in range(map_size)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(map_size):
    lst = list(map(int, input().split()))
    temp = max(lst)
    max_height = max(temp, max_height)
    _map.append(lst)

def raining(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != 0:
                map[i][j] -= 1

def find_from(map, x, y):
    if map[x][y] == 0:
        return False
    
    if visited[x][y]:
        return False
    
    global map_size
    q = Queue()
    q.put((x, y))
    visited[x][y] = True
    
    found = False
    if map[x][y] != 0:
        found = True

    while (not q.empty()):
        mx, my = q.get()
        for i in range(4):
            nx, ny = mx + dx[i], my + dy[i]
            if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size:
                continue

            if visited[nx][ny]:
                continue

            if map[nx][ny] == 0:
                continue

            found = True
            q.put((nx, ny))
            visited[nx][ny] = True
    return found

def find_all(map):
    global map_size
    count = 0
    for i in range(map_size):
        for j in range(map_size):
            if find_from(map, i, j):
                count += 1
    return count

max_count = -1

for i in range(max_height):
    max_count = max(max_count, find_all(_map))
    raining(_map)
    visited = [[False for _ in range(map_size)] for _ in range(map_size)]

print(max_count)