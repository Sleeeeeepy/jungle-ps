string = input()
a = string.count('a')
string += string[0:a-1]
_min = 2147483647
for i in range(len(string) - a + 1):
    _min = min(_min, string[i : (i+a)].count('b'))

print(_min)