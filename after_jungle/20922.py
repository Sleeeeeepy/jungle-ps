import sys
from collections import defaultdict

input = sys.stdin.readline
N, K = map(int, input().split())
numbers = list(map(int, input().split()))

start = 0
end = 0
duplication = defaultdict(int)
max_len = 0
while start < len(numbers) and end < len(numbers):
    if duplication[numbers[end]] < K:
        duplication[numbers[end]] += 1
        end += 1
    else:
        duplication[numbers[start]] -= 1
        start += 1
    max_len = max(max_len, abs(end - start))

print(max_len)