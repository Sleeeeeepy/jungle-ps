from collections import deque
debug = False
def rotate_left(gear: deque, idx: int):
    if debug: print(f'{idx} 반시계 회전')
    left = gear.popleft()
    gear.append(left)

def rotate_right(gear: deque, idx: int):
    if debug: print(f'{idx} 시계 회전')
    right = gear.pop()
    gear.appendleft(right)

def isS(n):
    return n == 1

def get_right_touched(gear: deque):
    return gear[2]

def get_left_touched(gear: deque):
    return gear[-2]

def get_score(gear: deque, factor: int):
    if isS(gear[0]):
        return 2 ** factor
    return 0

def is_turn_left(turn):
    return turn == -1

def turn_left():
    return -1

def turn_right():
    return 1

def rotate(toRotate, dir, gears):    
    last_left = get_left_touched(gears[toRotate])
    last_right = get_right_touched(gears[toRotate])
    last_right_dir = dir
    last_left_dir = dir
    if dir == -1:
        rotate_left(gears[toRotate], toRotate)
    else:
        rotate_right(gears[toRotate], toRotate)

    # Rotate right side first
    for i in range(toRotate + 1, 4):
        if last_right == get_left_touched(gears[i]):
            break
        last_right = get_right_touched(gears[i])
        if is_turn_left(last_right_dir):
            rotate_right(gears[i], i)
            last_right_dir = turn_right()
        else:
            rotate_left(gears[i], i)
            last_right_dir = turn_left()

    # Rotate left side
    for i in range(toRotate - 1, -1, -1):
        if last_left == get_right_touched(gears[i]):
            break
        last_left = get_left_touched(gears[i])
        if is_turn_left(last_left_dir):
            rotate_right(gears[i], i)
            last_left_dir = turn_right()
        else:
            rotate_left(gears[i], i)
            last_left_dir = turn_left()

gears = []
for i in range(4):
    gears.append(deque(list(map(int, list(input())))))

k = int(input())
for i in range(k):
    toRotate, dir = map(int, input().split())
    rotate(toRotate - 1, dir, gears)

score = 0
for idx, gear in enumerate(gears):
    score += get_score(gear, idx)

print(score)