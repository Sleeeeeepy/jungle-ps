n = int(input())
isPrime = [True] * (n + 1)
isPrime[0] = False
isPrime[1] = False

primes = []
for i in range(2, n + 1):
    if isPrime[i]:
        for j in range(i * 2, n + 1, i):
            isPrime[j] = False

for i in range(n + 1):
    if isPrime[i]:
        primes.append(i)

start = 0
end = 0
_sum = primes[0]
count = 0

while True:
    if _sum == n:
        count += 1
        _sum -= primes[start]
        start += 1
    elif _sum > n:
        _sum -= primes[start]
        start += 1
    else:
        end += 1
        _sum += primes[end]