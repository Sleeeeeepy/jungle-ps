import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
def bsearch(lst, start, end, num_to_find):
    if (start > end):
        return False
    
    mid = (start + end) // 2
    if lst[mid] == num_to_find: 
        return True
    elif lst[mid] > num_to_find:
        return bsearch(lst, start, mid-1, num_to_find)
    else:
        return bsearch(lst, mid+1, end, num_to_find)

input()
numbers = list(map(int, input().split()))
numbers.sort()

input()
nums_to_find = list(map(int, input().split()))

for i in nums_to_find:
    print("1") if bsearch(numbers, 0, len(numbers) - 1, i) else print("0")