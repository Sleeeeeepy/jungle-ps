import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

diff = 2147483647
start = 0
end = 1
while start < len(numbers) and end < len(numbers):
    if abs(numbers[start] - numbers[end]) == M:
        print(M)
        exit()
    elif abs(numbers[start] - numbers[end]) > M:
        diff = min(abs(numbers[start] - numbers[end]), diff)
        start += 1
    else:
        end += 1
    print(f'{start} {end}')
print(diff)