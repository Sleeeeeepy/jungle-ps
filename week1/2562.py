max = -1
index = 0

for i in range(9):
    number = int(input())
    if max < number:
        max = number
        index = i

print(max)
print(index + 1)