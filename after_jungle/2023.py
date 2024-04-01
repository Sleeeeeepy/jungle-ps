def isPrime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def find(number, N):
    if len(str(number)) == N:
        print(number)
        return
    
    for i in range(1, 10):
        if i % 2 == 0:
            continue

        if isPrime(number * 10 + i):
            find(number * 10 + i, N)
N = int(input())
find(2, N)
find(3, N)
find(5, N)
find(7, N)