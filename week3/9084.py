import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
num_testcase = int(input())

def test():
    num_coin_kinds = int(input())
    coins = list(map(int, input().split()))
    target_change = int(input())

    def solve(cursor, change):
        if change < 0:
            return 0
        
        if change == 0:
            return 1
        
        result = 0
        for i in range(cursor, num_coin_kinds):
            result += solve(i, change - coins[i])
        return result

    print(solve(0, target_change))

def test_memo():
    num_coin_kinds = int(input())
    coins = list(map(int, input().split()))
    target_change = int(input())
    dp = [[-1 for _ in range(10002)] for _ in range(22)]
    def solve(cursor, change):
        if change < 0:
            return 0
            
        
        if change == 0:
            return 1
        
        if dp[cursor][change] != -1:
            return dp[cursor][change]
        
        dp[cursor][change] = 0
        for i in range(cursor, num_coin_kinds):
            dp[cursor][change] += solve(i, change - coins[i])
        return dp[cursor][change]
    
    print(solve(0, target_change))


for i in range(num_testcase):
    test_memo()