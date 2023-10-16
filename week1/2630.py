import sys
input = sys.stdin.readline

size = int(input())
paper = []

for i in range(size):
    paper.append(list(map(int, input().split())))

num_white_paper = 0
num_blue_paper = 0
def find(startsAt, endsAt):
    global num_white_paper
    global num_blue_paper
    
    sx, sy = startsAt
    ex, ey = endsAt
    mx, my = (sx + ex) // 2, (sy + ey) // 2
    
    if (sx >= ex or sy >= ey):
        return
    
    is_same_color = True
    color = paper[sx][sy]
    for i in range(sx, ex):
        for j in range(sy, ey):
            if color != paper[i][j]:
                is_same_color = False
    
    if not is_same_color:
        find((sx, sy), (mx, my))
        find((sx, my), (mx, ey))
        find((mx, sy), (ex, my))
        find((mx, my), (ex, ey))
    else:
        if color == 0:
            num_white_paper += 1
        else:
            num_blue_paper += 1

find((0,0), (size, size))
print(num_white_paper)
print(num_blue_paper)