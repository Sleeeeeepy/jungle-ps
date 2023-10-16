import sys
input = sys.stdin.readline

num_words = int(input())
words = []

for i in range(num_words):
    words.append(input().split('\n')[0])

words = list(set(words))
words.sort(key=lambda x: [len(x), x])

for i in words:
    print(i)

