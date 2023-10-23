from collections import deque

num_coin, target_value = map(int, input().split())
coins = list(int(input()) for _ in range(num_coin))
memo = [0 for _ in range(10001)]
q = deque()

for i in range(num_coin):
    if coins[i] < 10001:
        memo[coins[i]] = 1
        q.append(coins[i])


def find():
    global num_coin 
    global target_value
    global q    

    while q:
        c = q.popleft()

        for i in range(num_coin):
            new_value = coins[i] + c
            if new_value < 10001:
                if memo[new_value] == 0:
                    memo[new_value] = memo[c] + 1
                    q.append(new_value)
find()
print(-1 if memo[target_value] == 0 else memo[target_value])