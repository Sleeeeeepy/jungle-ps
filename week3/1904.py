arr = [0, 1, 2]
n = int(input())

for i in range(3, n + 1):
    next = (arr[i - 2] + arr[i - 1]) % 15746
    arr.append(next)

print(arr[n])