year = int(input())
is_leap = False

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    is_leap = True

result = 1 if is_leap else 0
print(result)