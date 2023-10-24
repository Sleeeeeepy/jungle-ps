import sys
from collections import deque
input = sys.stdin.readline
num_marble, num_compare = map(int, input().split())

graph = [[0 for _ in range(num_marble)] for _ in range(num_marble)]
for i in range(num_compare):
    marble1, marble2 = map(int, input().split())
    graph[marble1 - 1][marble2 - 1] = 1

for k in range(num_marble):
    for i in range(num_marble):
        for j in range(num_marble):
            if graph[i][k] != 0 and graph[k][j] != 0:
                graph[i][j] = 1

count = 0
for i in range(num_marble):
    left = 0
    right = 0
    for j in range(num_marble):
        if i == j:
            continue

        if graph[i][j] == 1:
            right += 1
            continue

        if graph[j][i] == 1:
            left += 1
            continue

    if left > num_marble // 2 or right > num_marble // 2:
        count += 1

print(count)