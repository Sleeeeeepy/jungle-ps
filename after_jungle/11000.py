import heapq
N = int(input())
lecture = []
for i in range(N):
    start, end = map(int, input().split())
    lecture.append((start, end))

lecture.sort()
pq = []
heapq.heappush(pq, lecture[0][1])

for i in range(1, N):
    if lecture[i][0] < pq[0]:
        heapq.heappush(pq, lecture[i][1])
    else:
        heapq.heappop(pq)
        heapq.heappush(pq, lecture[i][1])

print(len(pq))