n = int(input())
pos = [0] * n
flag_a = [False] * n
flag_b = [False] * (n * 2) 
flag_c = [False] * (n * 2)
answer = 0

def place(position):
    global n
    global answer
    for i in range(n):
        if not flag_a[i] and not flag_b[position + i] and not flag_c[position - i + n - 1]:
            pos[position] = i
            if position == n - 1:
                answer += 1
            else:
                flag_a[i]= flag_b[position + i] = flag_c[position - i + n - 1] = True
                place(position + 1)
                flag_a[i]= flag_b[position + i] = flag_c[position - i + n - 1] = False

place(0)
print(answer)