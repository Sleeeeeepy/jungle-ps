import sys
input = sys.stdin.readline

num_numbers = int(input())
numbers = list(map(int, input().split()))
num_add, num_sub, num_mul, num_div = map(int, input().split())

_min = sys.maxsize
_max = -sys.maxsize

def find_minmax(current_number, add, sub, mul, div, result):
    global _min
    global _max

    if current_number == num_numbers - 1:
        _min = min(_min, result)
        _max = max(_max, result)
        return
    
    if add != 0:
        find_minmax(current_number + 1, add - 1, sub, mul, div, result + numbers[current_number + 1])

    if sub != 0:
        find_minmax(current_number + 1, add, sub - 1, mul, div, result - numbers[current_number + 1])

    if mul != 0:
        find_minmax(current_number + 1, add, sub, mul - 1, div, result * numbers[current_number + 1])

    if div != 0:
        if result < 0:
            temp = -result
            temp //= numbers[current_number + 1]
            temp = -temp
            find_minmax(current_number + 1, add, sub, mul, div - 1, temp)
        else:
            find_minmax(current_number + 1, add, sub, mul, div - 1, result // numbers[current_number + 1])

find_minmax(0, num_add, num_sub, num_mul, num_div, numbers[0])
print(_max)
print(_min)