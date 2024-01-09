import sys
input = sys.stdin.readline
size = int(input())
triangle = []

for _ in range(size):
    triangle.append(list(map(int, input().split())))

for i in range(1, size):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
            continue
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i - 1][j - 1]
            continue
        triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

print(max(triangle[size - 1]))