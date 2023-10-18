first = input()
second = input()

first_num = int(first)
result = []

for s in second:
    n = int(s)
    result.append(n * first_num)

result.reverse()
second_num = int(second)

for i in result:
    print(i)
print(first_num * second_num)