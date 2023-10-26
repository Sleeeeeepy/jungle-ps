fibonacci = [0, 1, 1]

n = int(input())

if n == 0:
    print(0)
    exit()

if n == 1:
    print(1)
    exit()

if n == 2:
    print(1)
    exit()

for i in range(n - 2):
    next_fibo = fibonacci[1] + fibonacci[2]
    fibonacci[0] = fibonacci[1]
    fibonacci[1] = fibonacci[2]
    fibonacci[2] = next_fibo

print(fibonacci[2])