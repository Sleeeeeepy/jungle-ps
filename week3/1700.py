import sys
input = sys.stdin.readline

num_socket, num_uses = map(int, input().split())
uses = list(map(int, input().split()))
socket = set()

answer = 0
for i in range(num_uses):
    # 이미 꽂힌 경우
    if uses[i] in socket:
        continue

    # 멀티탭이 비어있는 경우
    if len(socket) < num_socket:
        socket.add(uses[i])
        continue

    # 이미 멀티탭이 찬 경우
    # 꽂혀있는 전선 중 가장 오랫동안 사용하지 않는 것을 선택한다.
    victim = 0
    max_term = -1
    for j in socket:
        term = 0
        for k in range(i, num_uses):
            if j != uses[k]:
                term += 1
            else:
                break
        
        if max_term < term:
            victim = j
            max_term = term
    
    socket.remove(victim)
    socket.add(uses[i])
    answer += 1

print(answer)