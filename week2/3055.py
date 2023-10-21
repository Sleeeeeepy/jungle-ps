import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
forest = []

for i in range(r):
    forest.append(list(input().split('\n')[0]))

water = deque()
hedgehog = deque()

cave = (r - 1, c - 1)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if forest[i][j] == '*':
            water.append((i, j))
        elif forest[i][j] == 'D':
            cave = (i, j)
        elif forest[i][j] == 'S':
            hedgehog.append((i, j))

def can_move(graph, i, j) -> bool:
    global r
    global c
    if i < 0 or j < 0 or i >= r or j >= c:
        return False

    if graph[i][j] == '.' or graph[i][j] == 'D' or graph[i][j] == 'S':
        return True
    return False

def can_flood(graph, i, j) -> bool:
    global r
    global c
    if i < 0 or j < 0 or i >= r or j >= c:
        return False

    if graph[i][j] == '.' or graph[i][j] == 'S':
        return True
    return False

def flood(graph):
    new_flood = set()
    while water:
        x, y = water.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if can_flood(graph, nx, ny):
                graph[nx][ny] = '*'
                new_flood.add((nx, ny))

    for flood in new_flood:
        water.append(flood)

def runaway(graph):
    global r
    global c
    new_move = set()
    visited = [[False for _ in range(c)] for _ in range(r)] 
    found = False
    while hedgehog:
        # 잠긴 곳 제외
        x, y = hedgehog.popleft()
        if graph[x][y] == '*':
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not can_move(graph, nx, ny):
                continue

            if graph[nx][ny] == 'D':
                found = True
                graph[nx][ny] = 'S'
                break

            if not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = 'S'
                new_move.add((nx, ny))
    
    for move in new_move:
        hedgehog.append(move)

    return found

time = 0
prev = [['.' for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        prev[i][j] = forest[i][j]

while True:
    time += 1
    result = runaway(forest)
    flood(forest)
    if result:
        print(time)
        break
    is_done = True
    for i in range(r):
        for j in range(c):
            if forest[i][j] != prev[i][j]:
                is_done = False

    for i in range(r):
        for j in range(c):
            prev[i][j] = forest[i][j]
    if is_done:
        print("KAKTUS")
        break