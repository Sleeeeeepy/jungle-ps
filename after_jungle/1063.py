move = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1)
}

def to_coord(position):
    x = ord(position[0]) - ord('A')
    y = int(position[1]) - 1

    return (x, y)

def to_position(coord):
    x = chr(coord[0] + ord('A'))
    y = coord[1] + 1

    return x + f'{y}'

king, piece, N = input().split()
N = int(N)
king = to_coord(king)
piece = to_coord(piece)

def move_to(_from, dir):
    _to = move[dir]

    result = (_from[0] + _to[0], _from[1] + _to[1])
    if 0 <= result[0] < 8 and 0 <= result[1] < 8:
        return result
    return (-1, -1)

for i in range(N):
    dir = input()
    move_result = move_to(king, dir)
    if move_result[0] == -1:
        continue

    if move_result[0] == piece[0] and move_result[1] == piece[1]:
        piece_move_result = move_to(piece, dir)
        if piece_move_result[0] == -1:
            continue

        piece = piece_move_result
    king = move_result
print(to_position(king))
print(to_position(piece))