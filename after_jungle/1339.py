from collections import defaultdict
N = int(input())
terms = defaultdict(int)

for i in range(N):
    for idx, string in enumerate(input().rstrip()[::-1]):
        terms[string] += 10 ** idx

sorted_term = sorted(terms.items(), key=lambda x:x[1], reverse=True)
result = 0
i = 9
for term in sorted_term:
    result += term[1] * i
    i -= 1

print(result)