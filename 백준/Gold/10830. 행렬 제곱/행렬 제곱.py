import sys

N, B = map(int, sys.stdin.readline().strip().split())

A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

def matmul(U, V):
    W = [[sum(u * v for u, v in zip(U_row, V_col)) % 1000 for V_col in zip(*V)] for U_row in U]
    return W

def dc_pow(A, B):
    if B == 1:
        A = [[elem % 1000 for elem in rows] for rows in A]
        return A
    tmp = dc_pow(A, B//2)
    if B % 2: return matmul(matmul(tmp, tmp), A)
    else: return matmul(tmp, tmp)

C = dc_pow(A, B)
for c in C: print(*c)