import sys
input = sys.stdin.readline

num_coin_kind, target_change = map(int, input().split())
coins = [int(input()) for _ in range(num_coin_kind)] 
coins.sort(reverse=True)
current_change = target_change
num_coins = 0
for i in range(num_coin_kind):
    if current_change >= coins[i]:
        num_coins += current_change // coins[i]
        current_change %= coins[i]

print(num_coins)