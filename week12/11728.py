import sys
input = sys.stdin.readline
A = []

N, M = map(int, input().split())
A.extend(list(map(int, input().split())))
A.extend(list(map(int, input().split())))
A.sort()
print (*A, sep=' ')