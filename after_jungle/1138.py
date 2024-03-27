num_person = int(input())
people = list(map(int, input().split()))
answer = [0] * num_person

for i in range(num_person):
    cnt = 0
    for j in range(num_person):
        if cnt == people[i] and answer[j] == 0:
            answer[j] = i + 1
            break

        if answer[j] == 0:
            cnt += 1

print(*answer)