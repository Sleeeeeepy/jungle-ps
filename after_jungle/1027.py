def diff(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def count_buildings(startsAt, buildings):
    count = 0
    left = float('inf')
    right = -float('inf')
    for i in range(startsAt - 1, -1, -1):
        _diff = diff(i, buildings[i], startsAt, buildings[startsAt])
        if left > _diff:
            left = _diff
            count += 1
            continue

    for i in range(startsAt + 1, len(buildings)):
        _diff = diff(startsAt, buildings[startsAt], i, buildings[i])
        if right < _diff:
            right = _diff
            count += 1
            continue

    return count

num_buildings = int(input())
buildings = list(map(int, input().split()))
_max = -1

for i in range(len(buildings)):
    _max = max(count_buildings(i, buildings), _max)

print(_max)