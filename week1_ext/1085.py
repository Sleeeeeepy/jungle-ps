x, y, w, h = map(int, input().split())
shortest = min(abs(x - w), abs(y - h), x, y)
print(shortest)