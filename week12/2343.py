import sys
input = sys.stdin.readline

num_lectrue, num_bluray = map(int, input().split())
lectures = list(map(int, input().split()))

start = max(lectures)
end = sum(lectures)
answer = -1
while start <= end:
    mid = (start + end) // 2

    lecture_sum = 0
    count = 1
    for lecture in lectures:
        if lecture_sum + lecture > mid:
            count += 1
            lecture_sum = 0
        lecture_sum += lecture
    
    if num_bluray >= count:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)