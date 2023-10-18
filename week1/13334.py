from queue import PriorityQueue

pq = PriorityQueue()
num_men = int(input())
home_to_company = []
for i in range(num_men):
    x, y = map(int, input().split())
    if x > y:
        x = x ^ y
        y = x ^ y
        x = x ^ y
    home_to_company.append((x, y))

rail_length = int(input())
home_to_company.sort(key=lambda x:(x[1]))
answer = 0
current = 0
for i in range(num_men):
    # c에서 시작한다고 가정
    h, c = home_to_company[i]
    if abs(c - h) > rail_length:
        continue
    
    if c - rail_length <= h:
        current += 1
        pq.put(h)
    
    while not pq.empty():
        home = pq.get()
        if c - rail_length > home:
            current -= 1
            continue
        else:
            pq.put(home)
            break

    answer = max(current, answer)

print(answer)

