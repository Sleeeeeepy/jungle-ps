num_numbers = int(input())
numbers = list(map(int, input().split()))
is_not_prime = [False for _ in range(1001)]

is_not_prime[0] = True
is_not_prime[1] = True

for i in range(2, len(is_not_prime)):
    for j in range(2, len(is_not_prime)):
        if i == j:
            continue
        if i % j == 0:
            is_not_prime[i] = True
    i *= i
    
num_primes = 0
for i in numbers:
    if not is_not_prime[i]:
        num_primes += 1

print(num_primes)