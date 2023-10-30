import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
rocks = set()
for i in range(m):
    rocks.add(int(input()))

dp = [[float("inf") for _ in range(500)] for _ in range(n + 1)]
cnt = 0
def jump(current, jump_range):
    global n, m, cnt

    if current > n:
        return 2147483647

    if current == n:
        return 0
    
    if dp[current][jump_range] != float("inf"):
        return dp[current][jump_range]
    
    _min = 2147483647
    # 제자리 뛰기 방지
    if current + jump_range not in rocks and jump_range != 0:
        _min = min(_min, jump(current + jump_range, jump_range) + 1)

    # 뒤로 뛰기 방지
    if current + jump_range - 1 not in rocks and jump_range > 0:
        _min = min(_min, jump(current + jump_range - 1, jump_range - 1) + 1)

    if current + jump_range + 1 not in rocks:
        _min = min(_min, jump(current + jump_range + 1, jump_range + 1) + 1)

    dp[current][jump_range] = _min
    return dp[current][jump_range]

result = jump(1, 0)
print(result if result < 2147483647 else -1)