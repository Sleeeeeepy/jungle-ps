num_numbers = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
count = 0
for i in range(num_numbers):
    target = numbers[i]
    start = 0
    end = len(numbers) - 1

    while start < end:
        _sum = numbers[start] + numbers[end]
        if _sum == target:
            if start != i and end != i:
                count += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif _sum > target:
            end -= 1
        elif _sum < target:
            start += 1

print(count)