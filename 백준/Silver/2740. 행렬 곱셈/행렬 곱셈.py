import sys

N, M = map(int, sys.stdin.readline().strip().split())

A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

M, K = map(int, sys.stdin.readline().strip().split())

B = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

C = [[sum(A[n][m] * B[m][k] for m in range(M)) for k in range(K)] for n in range(N)]

for i in map(lambda x: ' '.join(map(str, x)), C): print(i)