import sys
input = sys.stdin.readline

matrix_size, exp = map(int, input().split())
matrix = []
for i in range(matrix_size):
    matrix.append(list(map(int, input().split())))

def pow(matrix, exp, mod):
    if exp == 0:
        # returns identity matrix
        size = len(matrix)
        ret = [[0] * size for _ in range(size)]
        for i in range(len(matrix)):
            ret[i][i] = 1
        return ret
    
    if exp == 1:
        return matrix_mod(matrix, mod)
    
    if exp % 2 == 0:
        result = pow(matrix, exp // 2, mod)
        return matrix_mult(result, result, mod)
    elif exp % 2 == 1:
        result = pow(matrix, exp // 2, mod)
        result_mat = matrix_mult(result, result, mod)
        return matrix_mult(result_mat, matrix, mod)
        
def matrix_mod(matrix, mod):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            matrix[i][j] %= mod
    return matrix

def matrix_mult(lhs, rhs, mod):
    size = len(lhs)
    temp_mat = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp = 0
            for k in range(size):
                temp += (lhs[i][k] % mod * rhs[k][j] % mod) % mod
            temp_mat[i][j] = temp % mod
    return temp_mat

result = pow(matrix, exp, 1000)
for arr in result:
    print(*arr)