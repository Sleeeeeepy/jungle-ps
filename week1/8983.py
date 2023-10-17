num_shooting_point, num_animal, gun_range = map(int, input().split())
shooting_points = list(map(int, input().split()))
animals = []
num_dead_aniaml = 0
shooting_points.sort()
for i in range(num_animal):
    x, y = map(int, input().split())
    animals.append((x, y))

# x의 어느 지점에 동물을 죽일수 있는 사대가 있는가?
def bsearch(animal, start, end):
    x, y = animal
    if start > end:
        return False
    
    mid = (start + end) // 2
    if can_kill(x, y, shooting_points[mid]):
        return True

    if x < shooting_points[mid]:
        return bsearch(animal, start, mid - 1)
    else:
        return bsearch(animal, mid + 1, end)

# 동물의 좌표와 사대의 본래 위치 shooting_point로 좌표를 계산합니다.
def can_kill(x, y, shooting_point):
    global gun_range
    result = gun_range - (abs(x - shooting_point))

    return result >= y

for animal in animals:
    if bsearch(animal, 0, len(shooting_points) - 1):
        num_dead_aniaml += 1

print(num_dead_aniaml)