import sys
input = sys.stdin.readline
dp = [[float("inf") for _ in range(501)] for _ in range(501)]
num_matrix = int(input())
matrix = []
for i in range(num_matrix):
    row, col = map(int, input().split())
    matrix.append((row, col))

#matrix chain multiplication
#clrs 15.2-2
count = 0
def matrix_chain_order(i, j):
    if (i == j):
        return 0

    if dp[i][j] != float("inf"):
        return dp[i][j]
    
    result = 2147483647
    for k in range(i, j):
        result = min(result, 
                     matrix_chain_order(i, k) +
                     matrix_chain_order(k + 1, j) +
                     matrix[i][0] * matrix[k][1] * matrix[j][1])
        
    dp[i][j] = result
    return dp[i][j]

print(matrix_chain_order(0, len(matrix) - 1))
