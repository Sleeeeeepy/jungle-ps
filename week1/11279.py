import sys
from queue import PriorityQueue
input = sys.stdin.readline

q = PriorityQueue()
num_inst = int(input())

for i in range(num_inst):
    inst = int(input())
    if inst == 0:
        if q.empty():
            print("0")
            continue
        print(-q.get())
        continue
    q.put(-inst)