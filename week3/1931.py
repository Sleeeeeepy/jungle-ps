rooms = []
num_rooms = int(input())
for i in range(num_rooms):
    start, end = map(int, input().split())
    rooms.append((start, end))

rooms.sort(key=lambda x : (x[1], x[0]))

end_time = 0
meets = 0
for i in range(len(rooms)):
    start, end = rooms[i]
    if start >= end_time:
        meets += 1
        end_time = end

print(meets)