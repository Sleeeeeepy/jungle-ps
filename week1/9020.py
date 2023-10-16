import math

is_prime = [True for _ in range(10_001)]
is_prime[0] = False
is_prime[1] = False

for i in range (2, int(math.sqrt(10_000)) + 1):
    if is_prime[i] == True:
        j = 2
        while i * j <= 10_000:
            is_prime[i * j] = False
            j += 1

num_test_case = int(input())
for _ in range(num_test_case):
    number = int(input())
    left = number // 2
    right = number // 2

    while left > 0 and right < 10001:
        if is_prime[left] and is_prime[right]:
            print(f"{left} {right}")
            break
        left -= 1
        right += 1