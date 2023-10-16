import sys
input = sys.stdin.readline

stack = []

num_command = int(input())

for i in range(num_command):
    command = input().split()
    
    if command[0] == "push":
        if command[1]:
            args1 = int(command[1])
            stack.append(args1)
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
            continue
        print("-1")
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if stack:
            print("0")
            continue
        print("1")
    elif command[0] == "top":
        if stack:
            print(stack[-1])
            continue
        print("-1")