import heapq
def solve(numbers):
    min_heap = []
    max_heap = []
    median = numbers[0]
    result = [median]
    for idx, number in enumerate(numbers[1:]):
        if number > median:
            heapq.heappush(min_heap, number)
        else:
            heapq.heappush(max_heap, -number)

        if idx % 2 == 1:
            if len(min_heap) < len(max_heap):
                heapq.heappush(min_heap, median)
                median = -heapq.heappop(max_heap)
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -median)
                median = heapq.heappop(min_heap)
            result.append(median)
    print(len(result))
    for idx, number in enumerate(result):
        if idx != 0 and idx % 10 == 0:
            print()
        print(number, end=' ')
num_testcase = int(input())
for i in range(num_testcase):
    num_numbers = int(input())
    numbers = []
    for _ in range(num_numbers // 10 + 1):
        numbers += list(map(int, input().split()))
    solve(numbers)
    print()