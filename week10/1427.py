import sys
input = sys.stdin.readline
numbers = list(input())
list.sort(numbers, reverse=True)

result = ""
for n in numbers:
    result += n

print(result)