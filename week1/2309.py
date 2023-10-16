
dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))
dwarfs.sort()

visited = [False for _ in range(9)]

def find_dwarfs(cursor, select, current_height):
    global found
    global visited
    if cursor == 9:
        return
    
    if current_height == 100 and select == 7:
        for i in range(9):
            if visited[i]:
                print(dwarfs[i])
        exit()
    
    if select == 7:
        return
    
    for i in range(9):
        if not visited[i]:
            visited[i] = True
            find_dwarfs(i, select + 1, current_height + dwarfs[i])
            visited[i] = False
            
find_dwarfs(0, 0, 0)