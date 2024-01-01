from functools import reduce
input()
lst = list(map(int, list(input())))
result = reduce(lambda x, y: x + y, lst)
print(result)