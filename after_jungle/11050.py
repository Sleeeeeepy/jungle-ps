import sys
N, K = map(int, input().split())

def get_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result

result = get_factorial(N) // (get_factorial(K) * get_factorial(N - K))
print(result)