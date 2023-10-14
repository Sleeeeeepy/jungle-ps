num_numbers = int(input())
numbers = []

for i in range(num_numbers):
    numbers.append(int(input()))

numbers.sort()

for i in numbers:
    print(i)