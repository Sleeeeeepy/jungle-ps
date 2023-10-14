N = int(input())
move_list = []
moves = 0

def hanoi(disk, _from, _to, _middle):
    global moves
    if disk == 1:
        move_list.append((f"{_from} {_to}"))
        moves += 1
        return
    
    hanoi(disk - 1, _from, _middle, _to)
    move_list.append((f"{_from} {_to}"))
    moves += 1
    hanoi(disk - 1, _middle, _to, _from)


if N <= 20:
    hanoi(N, 1, 3, 2)
    print(moves)
    for move_log in move_list:
        print(move_log)
else:
    print(2 ** N - 1)