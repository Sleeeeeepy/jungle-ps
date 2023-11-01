import sys
input = sys.stdin.readline

num_testcase = int(input())
def solve():
    num_people = int(input())
    scores = []
    for _ in range(num_people):
        score1, score2 = map(int, input().split())
        scores.append((score1, score2))
    
    scores.sort()
    _, best_rank = scores[0]
    answer = 1
    for i in range(num_people):
        if scores[i][1] < best_rank:
            answer += 1
            best_rank = scores[i][1]
    return answer

for i in range(num_testcase):
    answer = solve()
    print(answer)