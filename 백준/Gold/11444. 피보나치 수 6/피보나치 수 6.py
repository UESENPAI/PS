import sys

div = 1000000007

n = int(sys.stdin.readline().strip())

def matmul(U, V):
    W = [[sum(u * v for u, v in zip(U_row, V_col)) % div for V_col in zip(*V)] for U_row in U]
    return W

def dc_pow(A, B):
    if B == 1:
        A = [[elem % div for elem in rows] for rows in A]
        return A
    tmp = dc_pow(A, B//2)
    if B % 2: return matmul(matmul(tmp, tmp), A)
    else: return matmul(tmp, tmp)

A=[[1, 1], [1, 0]]
C = dc_pow(A, n)

print(C[1][0])