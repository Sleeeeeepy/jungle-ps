import sys
input = sys.stdin.readline

def compare(left, right):
    return left < right

def merge_sort(lst, start, end, comp):
    if start == end:
        return
    
    mid = (start + end) // 2
    merge_sort(lst, start, mid, comp)
    merge_sort(lst, mid + 1, end, comp)
    
    i = start
    j = mid + 1
    temp = []
    while i <= mid and j <= end:
        if comp(lst[i], lst[j]):
            temp.append(lst[i])
            i += 1
            continue

        temp.append(lst[j])
        j += 1
    
    while i <= mid:
        temp.append(lst[i])
        i += 1

    while j <= end:
        temp.append(lst[j])
        j += 1

    l = 0
    for k in range(start, end + 1):
        lst[k] = temp[l]
        l += 1

num_numbers = int(input())
numbers = []

for i in range(num_numbers):
    numbers.append(int(input()))

merge_sort(numbers, 0, len(numbers) - 1, compare)
for i in numbers:
    print(i)