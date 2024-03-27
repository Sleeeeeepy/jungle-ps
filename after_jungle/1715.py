from queue import PriorityQueue

num_stacks = int(input())
stacks = [int(input()) for _ in range(num_stacks)]
pq = PriorityQueue()

for i in stacks:
    pq.put(i)

stack1 = 0
stack2 = 0
_sum = 0

while pq.qsize() > 1:
    stack1 = pq.get()
    stack2 = pq.get()
    _sum += stack1 + stack2
    pq.put(stack1 + stack2)

print(_sum)