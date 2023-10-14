import sys
input = sys.stdin.readline

num_test_case = int(input())

for i in range(num_test_case):
    repeat, string = input().split()
    repeat = int(repeat)

    for j in range(len(string)):
        for k in range(repeat):
            print(string[j], end="")
    print("")
