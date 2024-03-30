N = int(input())

acc = 1
hexa = 0
hexa_numbers = []
while hexa < 1000001:
    hexa += acc
    acc += 4
    hexa_numbers.append(hexa)

dp = [0] * (N + 1)
for i in range(len(dp)):
    dp[i] = 6

dp[0] = 0
for i in range(1, N + 1):
    for j in range(len(hexa_numbers)):
        if i >= hexa_numbers[j]:
            dp[i] = min(dp[i], dp[i - hexa_numbers[j]] + 1)
            continue
        break
print(dp[N])