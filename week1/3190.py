from collections import deque

board_size = int(input())
num_apple = int(input())

board = [([0] * board_size) for _ in range(board_size)]
for _ in range(num_apple):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

num_moves = int(input())
moves = []
for _ in range(num_moves):
    time, dir = input().split()
    time = int(time)
    moves.append((time, dir))

snake = deque()
snake.append((0, 0))
board[0][0] = 2
RIGHT = [0, 1]
LEFT = [0, -1]
UP = [-1, 0]
DOWN = [1, 0]
DIR = [RIGHT, DOWN, LEFT, UP]
current_dir = 0

def change_dir(rotate_dir):
    global current_dir
    if rotate_dir == "L":
        current_dir = (4 + current_dir - 1) % 4
    elif rotate_dir == "D":
        current_dir = (current_dir + 1) % 4

time = 0
move = 0
over = False
while True:
    # 방향 확인
    if len(moves) > move and time == moves[move][0]:
        change_dir(moves[move][1])
        move += 1

    # 먼저 머리를 늘린다.
    x, y = snake.popleft()
    nx, ny = x + DIR[current_dir][0], y + DIR[current_dir][1]

    if nx < 0 or ny < 0 or nx >= board_size or ny >= board_size:
        # Game over
        print(time + 1)
        over = True
        break
    
    if (nx, ny) in snake:
        print(time + 1)
        over = True
        break

    # 사과가 있다면
    if board[nx][ny] == 1:
        snake.appendleft((x, y))
        snake.appendleft((nx, ny))
        board[nx][ny] = 2
        board[x][y] = 2
    else:
        snake.appendleft((x, y))
        snake.appendleft((nx, ny))
        board[nx][ny] = 2
        board[x][y] = 2
        px, py = snake.pop()
        board[px][py] = 0
    time += 1

if not over:
    print(time + 1)