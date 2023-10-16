# (A ** B) % C
A, B, C = map(int, input().split())

def pow(base, e, mod):
    if e == 0:
        return 1
    
    if e == 1:
        return base % mod
    
    mid = e // 2
    half = pow(base, mid, mod)

    if (e % 2 == 0):
        return half * half % mod
    return half * half % mod * base % mod

print(pow(A, B, C))